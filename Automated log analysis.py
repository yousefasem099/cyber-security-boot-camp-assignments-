
import re
import json

sql_pattern = re.compile(r"(\bSELECT\b.*\bFROM\b|\bUNION\b.*\bSELECT\b|' OR '1'='1)", re.IGNORECASE)

path_pattern = re.compile(r"(\.\./|%2e%2e%2f|%2e%2e/)", re.IGNORECASE)

ip_pattern = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

alerts = []

file = "access.log"

with open(file, "r") as f:
    lines = f.readlines()

for number, line in enumerate(lines, start=1):

    attack = ""

    if sql_pattern.search(line):
        attack = "SQL Injection"

    elif path_pattern.search(line):
        attack = "Path Traversal"

    if attack:
        ip = ip_pattern.search(line)

        if ip:
            address = ip.group()
        else:
            address = "Unknown"

        alert = {
            "line": number,
            "ip": address,
            "attack": attack
        }

        alerts.append(alert)

        print("Alert:", attack)
        print("IP:", address)
        print("Line:", number)
        print("----------------")

sql_count = sum(1 for x in alerts if x["attack"] == "SQL Injection")
path_count = sum(1 for x in alerts if x["attack"] == "Path Traversal")

print("\nAnalysis Summary")
print("Lines Scanned:", len(lines))
print("Suspicious Lines:", len(alerts))
print("SQL Injection:", sql_count)
print("Path Traversal:", path_count)
print("Normal Entries:", len(lines) - len(alerts))

with open("report.json", "w") as f:
    json.dump(alerts, f, indent=4)

print("\nJSON Report Saved Successfully.")
