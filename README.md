# 🔎 Filename Deception Detection with Data Science

## 📌 Project Overview
Phishing and malware campaigns often exploit **filename deception tricks** to trick users into opening harmful files.  
Examples include:
- Double extensions (e.g., `invoice.pdf.exe`)
- Unicode homoglyphs (`resumé.pdf` vs `resumé.pdf`)
- Invisible characters
- Random/obfuscated naming patterns

These tricks bypass casual inspection and even evade security filters.  
This project applies **Data Science + Machine Learning** to detect suspicious filenames automatically.

---

## 🗂️ Project Structure
```
Filename-Deception-Detection/
│── backend/        # Python backend (Flask / FastAPI) with ML model
│── frontend/       # React frontend for user interaction
│── README.md       # Project documentation
│── .gitignore      # Ignore unnecessary files
```

---

## ⚙️ Installation & Setup

### 🔹 Backend (Python)
1. Navigate to backend folder:
   ```bash
   cd backend
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   # Activate:
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the backend server:
   ```bash
   python app.py
   ```

---

### 🔹 Frontend (React)
1. Navigate to frontend folder:
   ```bash
   cd frontend
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm start
   ```

---

## 🔍 How It Works
1. User enters or uploads a filename in the frontend.
2. The request is sent to the backend API.
3. Backend applies **ML model** trained on the [Malicious File Trick Detection Dataset](https://www.kaggle.com/datasets/cyberprince/malicious-file-trick-detection-dataset/data).
4. The system extracts features like:
   - Number of dots/hyphens
   - Suspicious extensions
   - Unicode characters
   - Character n-grams
5. Model predicts **benign or suspicious**.
6. Result is returned and displayed in the frontend.

---

## 📊 Features
-  Detects **double extensions** and suspicious sequences  
-  Identifies **Unicode homoglyphs & invisible characters**  
-  Flags **random/obfuscated names** using character n-grams  
-  Machine Learning models: Logistic Regression, Decision Tree, Random Forest  
-  Explainability with **SHAP** (why a filename was flagged)  
-  Web interface for testing filenames interactively  

---

## 📈 Results
- **Accuracy:** 95.3%  
- **Precision:** 94.1%  
- **Recall:** 96.7%  
- **F1 Score:** 95.4%  

### Example Detection
- `invoice.pdf.exe` → **Malicious**  
- `document.txt` → **Safe**  
- `photo.jpg` → **Safe**  
- `salary_slip.pdf.scr` → **Malicious**  
- `update🔒.pdf` → **Malicious** (Unicode trick)  

---

## 🔮 Future Enhancements
- Expand to **file content analysis** (not just filenames)  
- Integrate into **email/file upload security systems**  
- Deploy as a **cloud-based API**  
- Add support for **real-time phishing email scanning**  

---

## 📚 References
- [Understanding File Masquerading in Phishing Attacks](https://cloudmersive.com/article/Understanding-File-Masquerading-in-Phishing-Attacks:-Detection-and-Protection)  
- [Unicode Homoglyph & Phishing Attacks](https://dmarcreport.com/blog/subtle-art-of-deception-homoglyphing-and-phishing-attacks/)  
- [Malicious File Trick Detection Dataset (Kaggle)](https://www.kaggle.com/datasets/cyberprince/malicious-file-trick-detection-dataset/data)  

---

## 👨‍💻 Author
**Harshit JK**  
📧 Mail: harshitjkvec2024to2028@gmail.com  


---

✨ *This project combines data science with cybersecurity — helping detect filename-based phishing and malware tricks before they reach end users.*
