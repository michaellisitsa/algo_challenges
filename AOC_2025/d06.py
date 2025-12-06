from pathlib import Path
import math
import re
from itertools import tee, chain


def pt1():
    with open(f"{Path(__file__).parent}/data/06.txt", "r") as f:
        arrays = []
        result = 0
        for line in f:
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


def pairwise(iterable, last_value=None):
    """
    Augmented pairwise which iterates over last value
    https://discuss.python.org/t/optionally-include-pair-of-last-and-first-element-of-iterator-in-itertools-pairwise/43382
    """
    a, b = tee(iterable)
    next(b, None)
    return zip(a, chain(b, [last_value]))


def pt2():
    with open(f"{Path(__file__).parent}/data/06.txt", "r") as f:
        arrays = []
        result = 0
        for line in f:
            if line[0] not in ["+", "*"]:
                arrays.append(line)
            else:
                # Assumes operator is on left-most column
                op_locs = [(m.start(0), m.group()) for m in re.finditer("[+*]", line)]

                for (start, op), (next_start, _) in pairwise(op_locs, (0, None)):
                    numbers = [
                        array[start : next_start - 1] for array in arrays
                    ]  # -1 as empty column between puzzles
                    vertical_numbers = [
                        int("".join(number[i] for number in numbers).strip())
                        for i in range(len(numbers[0]))
                    ]
                    result += (
                        sum(vertical_numbers)
                        if op == "+"
                        else math.prod(vertical_numbers)
                    )
        return result


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
