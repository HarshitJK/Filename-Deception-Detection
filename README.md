# 📘 Filename Deception Detection with Data Science  

### 🔒 Project Overview  
Phishing and malware campaigns often exploit **filename deception** to trick users into opening harmful files. Attackers use tricks like double extensions (`invoice.pdf.exe`), Unicode homoglyphs, invisible characters, and obfuscated names to disguise malicious files as safe.  

This project leverages **data science and machine learning** to automatically detect and flag suspicious filenames before they can harm users. A clean **web-based interface** is provided to scan, analyze, and review filename risks.  

---

## 🚀 Features  
✅ Detects **filename deception tricks**:  
- Double extensions  
- Unicode homoglyphs / invisible characters  
- Random / obfuscated strings  

✅ **Machine Learning–based classification** (Benign / Malicious / Medium risk)  
✅ **Confidence score** for each prediction  
✅ **Web dashboard** to upload and review scanned files  
✅ **Database download** of scan history  

---

## 🛠️ Tech Stack  
- **Frontend**: React.js, TailwindCSS  
- **Backend**: Flask (Python)  
- **Database**: SQLite  
- **ML / Data Science**: Pandas, NumPy, Scikit-learn, SHAP  

---

## 📂 Repository Structure  
```
Filename-Deception-Detection/
├── Backend/
│   ├── app.py
│   ├── requirements.txt
│   └── checked_files.db
├── Frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── Data/
│   └── Malicious_file_trick_detection.jsonl
├── Docs/
│   ├── Project_Report.pdf
│   ├── Project_Presentation.pptx
│   └── Screenshots/
│       ├── ui_dashboard.png
│       ├── scan_history.png
├── README.md
└── .gitignore
```

---

## 📊 Dataset  
- Used the **Malicious File Trick Detection Dataset** and manually created sample files for training/testing.  
- Examples:  
  - Benign → `document.txt`, `budget.xlsx`  
  - Malicious → `resume.docx.scr`, `vpn_setup.exe.txt`  

---

## 🔎 Data Science Process  
1. **Exploratory Data Analysis (EDA)** → Identify patterns like extra dots, Unicode anomalies, suspicious extensions.  
2. **Feature Engineering** → Character n-grams, number of special characters, double-extension flags.  
3. **Model Training** → Logistic Regression, Decision Trees, Random Forests.  
4. **Evaluation** → Accuracy, Precision, Recall, F1-score.  
5. **Explainability** → Used SHAP to highlight why a filename was flagged.  

---

## 📈 Results  
- High accuracy in detecting malicious filenames.  
- Low false negatives (priority to block risky files).  
- Visualization of common tricks (double extensions were most frequent).  

---

## 🖼️ Screenshots  

### 🔹 Dashboard – File Upload & Scan  
![UI Dashboard](Docs/Screenshots/ui_dashboard.png)  

### 🔹 History of Scanned Files  
![Scan History](Docs/Screenshots/scan_history.png)  

---

## ⚙️ How to Run  

### 🔧 Backend (Flask API)  
```bash
cd Backend
pip install -r requirements.txt
python app.py
```

### 💻 Frontend (React)  
```bash
cd Frontend
npm install
npm start
``` 

---

## 📌 Future Work  
- Extend detection to **file content analysis** (not just filename).  
- Integrate with **email scanning systems** to block phishing attachments.  
- Deploy as a **browser extension / cloud API**.  

---

## ✨ Contributors  
- **Harshit JK**  

---

👉 [**View Project Repository**](https://github.com/HarshitJK/Filename-Deception-Detection)  
