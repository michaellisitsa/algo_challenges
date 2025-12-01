from pathlib import Path
import re


def day01():
    with open(f"{Path(__file__).parent}/data/01.txt", "r") as f:
        dial = 50
        password = 0
        password2 = 0
        for idx, line in enumerate(f):
            direction = line[0]
            count = int(line[1:-1])
            count = count if direction == "R" else -count
            sum = dial + count
            remainder = abs(sum) % 100
            rotations = (abs(sum) - remainder) // 100
            if sum > 0:
                # if count > 99:
                # 0 -> 0 (rotations 0) = minus 0
                # 150 -> 50 (1 rotation) = minus 100
                # 100 -> 0 (1 rotation) = minus 100
                # 250 -> 50 (2 rotations) = minus 200
                dial = sum - (rotations * 100)
            elif sum < 0:
                # if count < 0:
                # -20 -> 80 (0 rotations) = plus 100
                # -99 -> 1 (0 rotations) = plus 100
                # -100 -> 0 (1 rotations) = plus 100
                # -101 -> 99 (1 rotations) = plus 200
                # -230 -> 70 (3 rotations) = plus 300
                rotations = rotations if remainder == 0 else rotations + 1
                dial = sum + (rotations * 100)
            else:
                dial = 0

            if dial == 0:
                password += 1
        return password


if __name__ == "__main__":
    print(day01())
