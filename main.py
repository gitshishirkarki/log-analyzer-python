from parser import read_logs
from analyzer import build_summary, filter_errors
from exporter import export_summary

def main() -> None:
    logs = read_logs("sample.log")
    summary = build_summary(logs)

    print("Summary:")
    print(summary)

    errors = filter_errors(logs)
    print("\nError logs:")
    for error in errors:
        print(error)

    export_summary(summary, "summary.json")
    print("\nsummary.json created")

if __name__ == "__main__":
    main()
