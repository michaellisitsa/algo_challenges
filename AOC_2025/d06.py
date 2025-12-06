from pathlib import Path
import math
import re


def pt1():
    with open(f"{Path(__file__).parent}/data/06.txt", "r") as f:
        arrays = []
        result = 0
        for idx, line in enumerate(f):
            numbers = re.findall("[0-9]+", line)
            if not arrays:
                arrays = [[int(num)] for num in numbers]
            elif numbers:
                for i, num in enumerate(numbers):
                    arrays[i].append(int(num))
            else:
                operators = re.findall("[*+]", line)
                for i, op in enumerate(operators):
                    match op:
                        case "*":
                            result += math.prod(arrays[i])
                        case "+":
                            result += sum(arrays[i])
        return result


def pt2():
    with open(f"{Path(__file__).parent}/data/06.txt", "r") as f:
        pass


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
