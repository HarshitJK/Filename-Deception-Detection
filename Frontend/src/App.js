import React, { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleUpload = async () => {
    if (!file) return;

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await fetch("http://127.0.0.1:5000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error("Error:", error);
      setResult({ error: "Could not connect to backend." });
    }
  };

  return (
    <div className="container">
      <h1>FileShield – Filename Deception Detection</h1>
      <footer className="footer">
  © Harshit JK
</footer>

     
    <div className="button-group">
  <input
    type="file"
    id="fileInput"
    onChange={handleFileChange}
    style={{ display: "none" }}
  />
  <label htmlFor="fileInput" className="custom-file-upload">
    📂 Choose File
  </label>

  <button onClick={handleUpload}>Analyze File</button>
</div>

{file && <span className="file-name">{file.name}</span>}

      {result && !result.error && (
        <div className={`result ${result.risk.toLowerCase()}`}>
          <h3>{result.filename}</h3>
          <p><b>Risk Level:</b> {result.risk}</p>
          <p><b>Score:</b> {result.score}</p>
          <ul>
            {result.reasons.map((r, i) => (
              <li key={i}>• {r}</li>
            ))}
          </ul>
        </div>
      )}

      {result && result.error && (
        <div className="result error">{result.error}</div>
      )}
    </div>
  );
}

export default App;
