from pathlib import Path
import re


def pt1():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        result = []
        for line in f:
            get_sum_expr(line)


def get_mul_expr(string: str):
    m = re.findall(r"mul\(\d+,\d+\)", string)
    print(f"{string=}")
    return m


if __name__ == "__main__":
    pt1()
