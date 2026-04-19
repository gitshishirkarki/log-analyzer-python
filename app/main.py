from fastapi import FastAPI, UploadFile, File, HTTPException
from app.analyzer import build_summary
from app.parser import parse_log_lines

from app.schemas import LogSummaryResponse

app = FastAPI(title= "Log Analyzer API")

@app.get("/")
def health_check() -> dict[str, str]:
    return {"message": "Log Analyzer API is running"}

@app.post("/analyze", response_model=LogSummaryResponse)
async def analyze_log(file: UploadFile=File(...)) -> LogSummaryResponse:
    if not file.filename.endswith(".log") and not file.filename.endswith(".txt"):
        raise HTTPException(status_code=400, detail="Only .log or .txt files are allowed")

    content =  await file.read()
    text = content.decode("UTF-8")
    lines = text.splitlines()
    logs, malformed_count = parse_log_lines(lines)
    summary = build_summary(logs, malformed_count)

    return LogSummaryResponse(**summary)