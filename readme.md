# Log Analyzer API (Python + FastAPI)

A simple log analysis service built with Python and FastAPI.

This project started as a CLI tool to learn Python basics and was extended into a backend API for practical usage.

---

## 🚀 Features

- Upload log files (`.log` / `.txt`)
- Parse structured log entries
- Count logs by level (INFO, WARN, ERROR)
- Count logs by service
- Filter logs using query parameters
- Detect malformed log lines
- Return structured JSON summary

---

## 🧠 Tech Stack

- Python
- FastAPI
- Pydantic
- Uvicorn

## ▶️ How to Run

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the server
```bash
uvicorn app.main:app --reload
```

