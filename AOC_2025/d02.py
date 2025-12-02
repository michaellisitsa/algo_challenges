from pathlib import Path
import typing as t


def divisorGenerator(n):
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            yield i


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def run():
    with open(f"{Path(__file__).parent}/data/02.txt", "r") as f:
        pt1 = 0
        pt2 = 0
        ranges = f.readline().strip("\n").split(",")
        for rng in ranges:
            start, _, end = rng.partition("-")
            print(f"{start=}")
            for id_num in range(int(start), int(end) + 1):
                id = str(id_num)
                if len(id) % 2 == 0 and id[: (len(id) // 2)] == id[(len(id) // 2) :]:
                    pt1 += int(id)
                found = False
                for divisor in divisorGenerator(len(id)):
                    value = id[:divisor]
                    if all([chunk == value for chunk in chunks(id, divisor)]):
                        found = True
                if found:
                    pt2 += int(id)

        return pt1, pt2


if __name__ == "__main__":
    print(run())
