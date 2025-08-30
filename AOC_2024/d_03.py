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


def pt2():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        result = []
        total = 0
        data = f.read().replace("\n", "")
        for do_string in slice_out_dos(data):
            pairs = get_mul_expr(do_string)
            for pair in pairs:
                total += mul_tuple(pair)
        return total


def slice_out_dos(string: str):
    # We need to figure out if the mul is preceded by a do() or start of string. But not preceded by don't.
    # Regex to just find don't, split by them, and then sum the strings that are do() groups.
    groups = string.split("don't()")
    dos = [groups.pop(0)]
    for group in groups:
        substring_index = group.find("do()")
        if substring_index != -1:
            dos.append(group[slice(substring_index, len(group))])
    return dos


def get_mul_expr(string: str):
    m = re.findall(r"mul\((\d+),(\d+)\)", string)
    return m


def mul_tuple(values: tuple[str, str]):
    a, b = values
    return int(a) * int(b)


if __name__ == "__main__":
    print(pt1())
    print(pt2())
