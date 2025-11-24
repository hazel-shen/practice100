# from collections import Counter
# with open('fruits.txt','r',encoding='utf-8') as f:
#     counts = Counter(line.strip() for line in f if line.strip())
# print('\n'.join(f"{k}: {v}" for k,v in counts.items()))

counts = {}
with open('fruits.txt', 'r', encoding='utf-8') as f:
    for line in f:
        key = line.strip()
        if not key:
            continue
        counts[key] = counts.get(key, 0) + 1

for k, v in counts.items():
    print(f"{k} {v}")

print(counts.keys())
print(counts.values())
print(counts.items())