from collections import Counter
from app.models import LogEntry


def count_by_level(logs: list[LogEntry]) -> dict[str, int]:
    return dict(Counter(log.level for log in logs))

def count_by_service(logs: list[LogEntry]) -> dict[str, int]:
    return dict(Counter(log.service for log in logs))

def filter_errors(logs: list[LogEntry]) -> list[LogEntry]:
    return [log for log in logs if log.level == "ERROR"]

def count_error_messages(logs: list[LogEntry]) -> dict[str, int]:
    error_logs = [log for log in logs if log.level == "ERROR"]
    return dict(Counter(log.message for log in error_logs))

def build_summary(logs: list[LogEntry], malformed_count: int) -> dict:
    return {
        "total_logs": len(logs),
        "malformed_lines": malformed_count,
        "count_by_level": count_by_level(logs),
        "count_by_service": count_by_service(logs),
        "error_messages": count_error_messages(logs)
    }
