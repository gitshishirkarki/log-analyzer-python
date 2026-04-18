import json

def export_summary(summary: dict, output_file: str) -> None:
    with open(output_file, "w", encoding="UTF-8") as file:
        json.dump(summary, file, indent=4)