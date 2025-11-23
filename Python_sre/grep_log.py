from datetime import datetime, timedelta
import re

now = datetime.now()
target_time = now - timedelta(minutes=30)

with open("/var/log/nginx/access.log", "r") as f:
    for line in f:
        if "404" in line:
            match = re.search(r"\[(\d+/[A-Za-z]+/\d+:\d+:\d+:\d+)", line)
            log_time_str = match.group(1)  # e.g. "30/Jul/2025:21:28:41"
            log_time = datetime.strptime(log_time_str, "%d/%b/%Y:%H:%M:%S")
            parts = line.split()
            ip = parts[0]
            url = parts[6]
            print(f"{log_time.strftime('%Y-%m-%d %H:%M:%S')} - {ip} - {url}")


