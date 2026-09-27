def month_calendar(start_weekday, days):
    result = []

    for i in range(start_weekday):
        result.append("  ")
    for day in range(1, days + 1):
        result.append(f"{day:2}")
    lines = []
    for i in range(0, len(result), 7):
        line = " ".join(result[i:i + 7]).rstrip()
        lines.append(line)
    return "\n".join(lines)

print(month_calendar(6, 31))