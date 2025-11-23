import subprocess
import json
from collections import Counter

result = subprocess.run(
    ["jq", ".[] | select(.status >= 400)", "waf_logs.json"],
    capture_output = True,
    text = True,
    check = True
)

lines = result.stdout.strip().split('\n')
json_objects = [json.loads(line) for line in lines]

counter = Counter(log["status"] for log in json_objects)

for status, count in counter.items():
    print(f"{status}: {count}")
