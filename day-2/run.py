with open('input', 'r') as file:
    safe_reports = 0
    for line in file:
        report = list(map(int, line.strip().split(" ")))
        increasing = all(1 <= report[i + 1] - report[i] <= 3 for i in range(len(report) - 1))
        decreasing = all(-3 <= report[i + 1] - report[i] <= -1 for i in range(len(report) - 1))
        if increasing or decreasing:
            safe_reports += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                increasing = all(1 <= modified_report[j + 1] - modified_report[j] <= 3 for j in range(len(modified_report) - 1))
                decreasing = all(-3 <= modified_report[j + 1] - modified_report[j] <= -1 for j in range(len(modified_report) - 1))
                if increasing or decreasing:
                    safe_reports += 1
                    break
    print(safe_reports)

