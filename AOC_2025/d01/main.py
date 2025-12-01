from pathlib import Path
import re

# Error
# line='R36\n' direction='R' count=36
# dial prev 91 after 27 sum 127
# password=887
# line='L127\n' direction='L' count=-127
# dial prev 27 after 100 sum -100
# password=887


def day01():
    with open(f"{Path(__file__).parent}/data/01.txt", "r") as f:
        dial = 50
        password = 0
        for idx, line in enumerate(f):
            # print(f"{idx=}")
            # if idx > 85:
            #     break
            direction = line[0]
            count = line[1:-1]
            count = int(count) if direction == "R" else -int(count)
            # You want to loop over the 99 point.
            # If number is greater than 99, e.g. 50 + 100, then minus (number % 100)*100 from it
            # Example: (150 % 100).
            sum = dial + count
            # 150 -> 50
            remainder = abs(sum) % 100
            # rotations = (sum - remainder) // 100
            # sum = -20,
            rotations = (abs(sum) - remainder) // 100
            # print(f"{line=} {direction=} {count=}")
            # print("dial prev", dial, "sum", sum)
            prev_dial = dial
            if sum > 0:
                dial = sum - (rotations * 100)
                # if count > 99:
                # 150 -> 50 = minus 100 1 rotation
                # 100 -> 0 = minus 100 1 rotation
                # 250 -> 50 = minus 200 2 rotations
            elif sum < 0:
                # if count < 0:
                # from 5, went to -20. Rotations is zero. We need to go to 80. -> 80 = plus 100
                # -100 -> 0 = plus 100
                # -230 -> 70 = plus 200
                # for sum = -100
                # -100 + (1+1)*100
                dial = sum + (rotations * 100)
            else:
                # print(f"{line=} {direction=} {count=}")
                # print("dial prev", dial, "sum", sum)
                dial = 0
                # print("dial after", dial)
            if dial == 0:
                password += 1
                # print(f"{rotations=}")
            print(f"{line=} {direction=} {count=}")
            print("dial prev", prev_dial, "after", dial, "sum", sum)
            print(f"{password=}")
            # if rotations > 1:
            #     print(f"{dial=}")
            # print("dial after", dial)
            # print(f"{rotations=}")
        print(f"{password=}")


if __name__ == "__main__":
    day01()
