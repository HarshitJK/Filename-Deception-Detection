import json
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

data = []

# --- Safe JSONL loader ---
with open("Malicious_file_trick_detection.jsonl", "r", encoding="utf-8", errors="ignore") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
            if "filename" in record:
                data.append({"filename": record["filename"], "label": "malicious"})
        except json.JSONDecodeError as e:
            print(f"⚠️ Skipping bad line {i}: {e}")

# Add synthetic benign samples
# Load benign samples
with open("benign_samples.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line.strip())
        if "filename" in record:
            data.append(record)

# --- Train ML model ---
df = pd.DataFrame(data)
X = df["filename"]
y = df["label"]

vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(2,5))
X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=2000)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save model + vectorizer
joblib.dump(model, "filename_model.pkl")
joblib.dump(vectorizer, "filename_vectorizer.pkl")
print("✅ Model and vectorizer saved!")
