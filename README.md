# Security Log Analysis

## Project Overview

This project demonstrates a basic cybersecurity log analysis process used to identify suspicious authentication activity within a network environment.

## Objective

Analyze authentication logs and identify potential security incidents, suspicious login attempts, and indicators of brute-force attacks.

## Scenario

A security analyst was tasked with reviewing authentication logs to determine whether any suspicious activity was present.

## Findings

* Multiple failed login attempts were detected from IP address **10.0.0.25**
* The account **guest** generated four failed authentication attempts
* Repeated failures may indicate a potential brute-force attack
* Legitimate successful logins were also identified

## Files Included

### sample_logs.txt

Contains sample authentication log entries.

### analysis.md

Contains the investigation findings and recommendations.

## Skills Demonstrated

* Cybersecurity
* Security Analysis
* Log Analysis
* Incident Detection
* Threat Identification
* Risk Assessment
* Security Monitoring

## Recommendations

* Investigate the source IP address
* Monitor future authentication attempts
* Implement account lockout policies
* Review authentication controls

## Author

Ismail Amoud

## Python Automation

This project includes a Python-based log analysis tool capable of:

- Parsing authentication logs
- Identifying failed login attempts
- Summarizing suspicious authentication activity
- Supporting basic security investigations

## Key Achievement

Developed a Python-based log analysis tool to identify failed authentication attempts and summarize suspicious login activity.

## Technologies Used

- Python
- GitHub
- Log Analysis
- Cybersecurity
- Security Monitoring

## Project Output

Example of the script detecting suspicious authentication activity and generating an automated security report.

![Security Log Output](image.png)
