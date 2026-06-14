log_file = "sample_logs.txt"

failed_attempts = {}

with open(log_file, "r") as file:

    for line in file:

        if "FAILED" in line:

            parts = line.split()

            user = parts[3]
            ip = parts[4]

            if ip not in failed_attempts:
                failed_attempts[ip] = 0

            failed_attempts[ip] += 1

print("=== Failed Login Summary ===")

for ip, count in failed_attempts.items():
    print(f"{ip} : {count} failed attempts")
