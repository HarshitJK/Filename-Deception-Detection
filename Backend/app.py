from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)  # allow frontend (React) to talk to backend

# --- Detection Logic ---
dangerous_exts = ["exe","js","vbs","scr","bat","cmd","jar","ps1","apk","msi","lnk","iso","hta","wsf","dll"]
safe_mask_exts = ["pdf","doc","docx","xls","xlsx","ppt","pptx","txt","jpg","jpeg","png","gif","zip","rar","7z"]

def get_ext(name):
    parts = name.split(".")
    return parts[-1].lower() if len(parts) > 1 else ""

def has_double_extension(name):
    return bool(re.search(rf"\.({'|'.join(safe_mask_exts)})\s*\.+\s*({'|'.join(dangerous_exts)})$", name.lower()))

def has_rlo(name):
    return "\u202e" in name

def has_long_whitespace(name):
    return bool(re.search(rf"\s{{6,}}\.+\s*({'|'.join(dangerous_exts)})$", name.lower()))

def is_dangerous_ext(name):
    return get_ext(name) in dangerous_exts

def score_filename(name):
    score, reasons = 0, []
    if is_dangerous_ext(name):
        score += 30; reasons.append("Dangerous extension")
    if has_double_extension(name):
        score += 25; reasons.append("Double extension trick")
    if has_rlo(name):
        score += 20; reasons.append("RLO (Right-to-Left override)")
    if has_long_whitespace(name):
        score += 10; reasons.append("Whitespace padding")
    return score, reasons

# --- Routes ---
@app.route("/", methods=["GET"])
def home():
    return "✅ Flask backend is running! Use POST /analyze to check files."

@app.route("/analyze", methods=["POST"])
def analyze():
    if "file" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    f = request.files["file"]
    filename = f.filename

    score, reasons = score_filename(filename)
    if score >= 50:
        risk = "High"
    elif score >= 25:
        risk = "Medium"
    else:
        risk = "Low"

    return jsonify({
        "filename": filename,
        "score": score,
        "risk": risk,
        "reasons": reasons
    })

if __name__ == "__main__":
    app.run(debug=True)
