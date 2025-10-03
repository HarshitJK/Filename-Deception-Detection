import React, { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);

  useEffect(() => {
    fetchHistory();
  }, []);

  const fetchHistory = async () => {
    const res = await fetch("http://localhost:5000/files");
    const data = await res.json();
    setHistory(data);
  };

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) return;
    setLoading(true);

    const formData = new FormData();
    formData.append("file", file);

    const res = await fetch("http://localhost:5000/analyze", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    setResult(data);
    setLoading(false);
    fetchHistory(); // refresh history after new upload
  };

  return (
    <div className="app-container">
      <h1 className="title">🛡️ Filename Deception Detector</h1>
      <p className="subtitle">Upload a file and check if it’s safe</p>

      <div className="upload-box">
        <input type="file" onChange={handleFileChange} />
        <button className="btn" onClick={handleSubmit} disabled={loading}>
          {loading ? "Analyzing..." : "Analyze File"}
        </button>
      </div>

      {result && (
        <div className="result-card">
          <h2>📊 Latest Analysis</h2>
          <table>
            <tbody>
              <tr><td>📄 Filename</td><td>{result.filename}</td></tr>
              <tr><td>🔍 Prediction</td><td className={`badge ${result.prediction}`}>{result.prediction}</td></tr>
              <tr><td>📈 Confidence</td><td>{(result.confidence * 100).toFixed(2)}%</td></tr>
              <tr><td>⚠️ Risk</td><td className={`badge ${result.risk.toLowerCase()}`}>{result.risk}</td></tr>
              <tr><td>🎭 Tricks</td><td>{result.detected_tricks}</td></tr>
              <tr><td>📂 Extension</td><td>{result.extension_category}</td></tr>
              <tr><td>🔢 Length</td><td>{result.filename_length}</td></tr>
              <tr><td>⏰ Checked At</td><td>{new Date(result.created_at).toLocaleString()}</td></tr>
            </tbody>
          </table>
        </div>
      )}

      <div className="history-card">
  <h2>📜 History of Scanned Files</h2>
  <button
    className="btn download-btn"
    onClick={() => (window.location.href = "http://localhost:5000/download-db")}
  >
    ⬇️ Download Database
  </button>
  <table className="history-table">
    <thead>
      <tr>
        <th>Filename</th>
        <th>Prediction</th>
        <th>Risk</th>
        <th>Confidence</th>
        <th>Tricks</th>
      </tr>
    </thead>
    <tbody>
      {history.map((file) => (
        <tr key={file.id}>
          <td>{file.filename}</td>
          <td className={`text-${file.prediction.toLowerCase()}`}>
            {file.prediction}
          </td>
          <td className={`text-${file.risk.toLowerCase()}`}>
            {file.risk}
          </td>
          <td>{(file.confidence * 100).toFixed(1)}%</td>
          <td>{file.detected_tricks}</td>
        </tr>
      ))}
    </tbody>
  </table>
</div>

    </div>
  );
}

export default App;
