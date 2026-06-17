log_file = "sample_logs.txt"
report_file = "report.txt"

failed_attempts = {}
suspicious_ips = {}

with open(log_file, "r") as file:
    for line in file:
        if "FAILED" in line:
            parts = line.split()
            user = parts[3]
            ip = parts[4]

            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] += 1

print("\n=== Failed Login Summary ===\n")

for ip, count in failed_attempts.items():
    print(f"{ip} : {count} failed attempts")

print("\n=== Suspicious Activity ===\n")

for ip, count in failed_attempts.items():
    if count >= 3:
        suspicious_ips[ip] = count
        print(f"ALERT: {ip} generated {count} failed login attempts")

with open(report_file, "w") as report:
    report.write("Security Log Analysis Report\n")
    report.write("============================\n\n")

    report.write("Failed Login Summary\n")
    report.write("--------------------\n")

    for ip, count in failed_attempts.items():
        report.write(f"{ip} : {count} failed attempts\n")

    report.write("\nSuspicious Activity\n")
    report.write("-------------------\n")

    if suspicious_ips:
        for ip, count in suspicious_ips.items():
            report.write(f"ALERT: {ip} generated {count} failed login attempts\n")
    else:
        report.write("No suspicious activity detected.\n")

print("\nReport generated successfully: report.txt")
