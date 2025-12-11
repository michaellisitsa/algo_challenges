from pathlib import Path
from itertools import combinations


def run():
    with open(f"{Path(__file__).parent}/data/09.txt", "r") as f:
        inputs = []
        for idx, line in enumerate(f):
            inputs.append([int(coord) for coord in line.rstrip().split(",")])
        max_A = 0
        for pt1, pt2 in combinations(inputs, 2):
            A = (max(pt1[0], pt2[0]) - min(pt1[0], pt2[0]) + 1) * (
                max(pt1[1], pt2[1]) - min(pt1[1], pt2[1]) + 1
            )
            if A > max_A:
                max_A = A
        return max_A


if __name__ == "__main__":
    print(run())
