from pathlib import Path

col1 = []
col2 = []

with open(f"{Path(__file__).parent}/data/01.txt", "r") as f:
    for idx, line in enumerate(f):
        val1, val2 = line.split()
        col1.append(val1)
        col2.append(val2)
    col1.sort()
    col2.sort()

sum = 0
for val1, val2 in zip(col1, col2):
    sum += abs(int(val1) - int(val2))
