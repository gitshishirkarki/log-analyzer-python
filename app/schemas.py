from pydantic import BaseModel

class LogSummaryResponse(BaseModel):
    total_logs: int
    malformed_lines: int
    count_by_level: dict[str, int]
    count_by_service: dict[str, int]
    error_messages: dict[str, int]