from pathlib import Path
import re


def pt1():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        result = []
        total = 0
        for line in f:
            pairs = get_mul_expr(line)
            for pair in pairs:
                total += mul_tuple(pair)
        return total


def get_mul_expr(string: str):
    m = re.findall(r"mul\((\d+),(\d+)\)", string)
    return m


def mul_tuple(values: tuple[str, str]):
    a, b = values
    return int(a) * int(b)


if __name__ == "__main__":
    print(pt1())
