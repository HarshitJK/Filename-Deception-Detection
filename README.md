# Filename Deception Detection with Data Science

## 📌 Project Overview
Phishing and malware campaigns often use filename tricks (e.g., `invoice.pdf.exe`, Unicode homoglyphs, invisible characters).
This project applies **data science + machine learning** to detect such deceptive filenames.

## 🔍 Features
- Detects suspicious filename patterns
- Handles Unicode homoglyph & double extensions
- Uses ML models like Logistic Regression & Decision Tree
- Explainability with SHAP

## 📂 Project Structure
- `data/` → Dataset files
- `src/` → Source code & model training scripts
- `docs/` → Reports & presentations
- `models/` → Trained models (if any)

## 🚀 Usage
```bash
pip install -r requirements.txt
python src/train_model.py
