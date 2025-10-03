from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import joblib, os, datetime, re
from flask import send_file

app = Flask(__name__)
CORS(app)

# ------------------ Database Config ------------------
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "checked_files.db")
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# ------------------ Database Model ------------------
class CheckedFile(db.Model):
    __tablename__ = "checked_files"
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(512), nullable=False)
    prediction = db.Column(db.String(50), nullable=False)
    confidence = db.Column(db.Float, nullable=False)
    risk = db.Column(db.String(50), nullable=False)
    detected_tricks = db.Column(db.String(200), nullable=True)
    extension_category = db.Column(db.String(50), nullable=True)
    filename_length = db.Column(db.Integer, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "filename": self.filename,
            "prediction": self.prediction,
            "confidence": self.confidence,
            "risk": self.risk,
            "detected_tricks": self.detected_tricks,
            "extension_category": self.extension_category,
            "filename_length": self.filename_length,
            "created_at": self.created_at.isoformat()
        }

# ------------------ Load Model ------------------
model = joblib.load("filename_model.pkl")
vectorizer = joblib.load("filename_vectorizer.pkl")

# ------------------ Risk level function ------------------
def get_risk(prediction, confidence):
    if prediction == "malicious":
        if confidence >= 0.75:
            return "High"
        if confidence >= 0.5:
            return "Medium"
        return "Low"
    return "Low"

# ------------------ Helper functions ------------------
def detect_tricks(filename: str) -> str:
    tricks = []
    if len(filename.split(".")) > 2:
        tricks.append("double_extension")
    if any(ord(c) > 127 for c in filename):
        tricks.append("unicode_or_invisible")
    if re.search(r"[0-9]{4,}", filename) or re.search(r"[A-Z]{4,}", filename):
        tricks.append("random_string")
    return ",".join(tricks) if tricks else "none"

def categorize_extension(filename: str) -> str:
    ext = filename.split(".")[-1].lower()
    dangerous_ext = {"exe", "scr", "bat", "js", "vbs"}
    document_ext = {"pdf", "doc", "docx", "txt", "xls", "xlsx"}
    compressed_ext = {"zip", "rar", "7z", "tar", "gz"}
    if ext in dangerous_ext:
        return "dangerous"
    elif ext in document_ext:
        return "document"
    elif ext in compressed_ext:
        return "compressed"
    else:
        return "other"

# ------------------ Routes ------------------
@app.route("/", methods=["GET"])
def home():
    return "Flask ML backend with DB is running!"

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    f = request.files["file"]
    filename = f.filename

    # ML prediction
    X = vectorizer.transform([filename])
    prediction = model.predict(X)[0]
    confidence = float(model.predict_proba(X).max())
    risk = get_risk(prediction, confidence)

    # Extract behavior data
    tricks = detect_tricks(filename)
    ext_category = categorize_extension(filename)
    name_length = len(filename)

    # Save to DB
    record = CheckedFile(
        filename=filename,
        prediction=prediction,
        confidence=confidence,
        risk=risk,
        detected_tricks=tricks,
        extension_category=ext_category,
        filename_length=name_length
    )
    db.session.add(record)
    db.session.commit()

    return jsonify(record.to_dict())

@app.route("/download-db", methods=["GET"])
def download_db():
    return send_file(DB_PATH, as_attachment=True)


@app.route("/files", methods=["GET"])
def list_files():
    files = CheckedFile.query.order_by(CheckedFile.created_at.desc()).all()
    return jsonify([f.to_dict() for f in files])

# ------------------ Main ------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
