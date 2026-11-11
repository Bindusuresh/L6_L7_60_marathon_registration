
def format_bib_name(name):
    """Safely formats a runner's name for the bib."""
    if not isinstance(name, str):
        return ""

    return name.strip().upper()[:12]


def parse_finish_time(text):
    """Safely converts H:MM:SS into seconds."""
    if not isinstance(text, str):
        return None

    parts = text.split(':')

    if len(parts) != 3:
        return None

    try:
        hours, minutes, seconds = map(int, parts)

        if hours < 0 or minutes < 0 or seconds < 0:
            return None

        if minutes > 59 or seconds > 59:
            return None

        return hours * 3600 + minutes * 60 + seconds

    except (ValueError, TypeError, OverflowError):
        return None


def average_split(text):
    """Safely calculates the average of split times."""
    if not isinstance(text, str):
        return None

    parts = text.split()

    if not parts:
        return None

    try:
        splits = [int(s) for s in parts]

        if any(s < 0 for s in splits):
            return None

        return sum(splits) / len(splits)

    except (ValueError, TypeError, OverflowError):
        return None


def main():
    print("==== Running format_bib_name ====")
    value = input("Enter the name to print on the bib: ")
    print("Bib name:", format_bib_name(value))

    print("\n==== Running parse_finish_time ====")
    value = input("Enter a finish time as H:MM:SS (e.g. 3:45:10): ")
    result = parse_finish_time(value)
    print("Finish time in seconds:", result if result is not None else "Invalid finish time")

    print("\n==== Running average_split ====")
    value = input("Enter your 5 km split times in minutes separated by spaces (e.g. 25 26 24): ")
    result = average_split(value)
    print("Average split (minutes):", result if result is not None else "Invalid split times")


if __name__ == "__main__":
    main()
