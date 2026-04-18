from collections import Counter
from models import LogEntry


def count_by_level(logs: list[LogEntry]) -> dict[str, int]:
    return dict(Counter(log.level for log in logs))

def count_by_service(logs: list[LogEntry]) -> dict[str, int]:
    return dict(Counter(log.service for log in logs))

def filter_errors(logs: list[LogEntry]) -> list[LogEntry]:
    return [log for log in logs if log.level == "ERROR"]

def build_summary(logs: list[LogEntry]) -> dict:
    return {
        "total_logs": len(logs),
        "count_by_level": count_by_level(logs),
        "count_by_service": count_by_service(logs),
        "total_errors": len(filter_errors(logs))
    }
