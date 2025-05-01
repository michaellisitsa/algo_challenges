from pathlib import Path

col1 = []
col2 = []
col1_set = set()

with open(f"{Path(__file__).parent}/data/01.txt", "r") as f:
    for idx, line in enumerate(f):
        val1, val2 = line.split()
        # Create 2 list for later sorting
        # for part 1
        col1.append(val1)
        col2.append(val2)
        # Create a unique set of left col values for later matching with col2
        # to solve part 2
        col1_set.add(val1)

# Pt 1
col1.sort()
col2.sort()
sum = 0
for val1, val2 in zip(col1, col2):
    sum += abs(int(val1) - int(val2))

# Pt 2
col1_matchers = dict.fromkeys(col1_set)
for value in col2:
    if value in col1_matchers:
        col1_matchers[value] = (col1_matchers[value] or 0) + 1

sum_pt2 = 0
for key, value in col1_matchers.items():
    if value is not None:
        sum_pt2 += int(key) * value

print(f"soln: Pt1:{sum}, Pt2:{sum_pt2}")
