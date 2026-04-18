from models import LogEntry

def parse_log_line(line: str) -> LogEntry | None:
    parts = line.strip().split(" ", 4)
    if len(parts) < 5:
        return None
    
    timestamp = f"{parts[0]} {parts[1]}"
    level = parts[2]
    service = parts[3]
    message = parts[4]

    return LogEntry(
        timestamp=timestamp,
        level=level,
        service=service,
        message=message
    )

def read_logs(file_path: str) -> list[LogEntry]:
    logs: list[LogEntry] = []

    with open(file_path, "r", encoding="UTF-8") as file:
        for line in file:
            entry = parse_log_line(line)
            if entry is not None:
                logs.append(entry)
    
    return logs