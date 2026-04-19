from app.models import LogEntry

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

def parse_log_lines(lines: list[str]) -> tuple[list[LogEntry]]:
    logs: list[LogEntry] = []
    malformed_count = 0

    for line in lines:
        entry = parse_log_line(line)
        if entry is not None:
            logs.append(entry)
        else:
            malformed_count += 1
    
    return logs, malformed_count