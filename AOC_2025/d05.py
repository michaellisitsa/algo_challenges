from pathlib import Path


def run():
    with open(f"{Path(__file__).parent}/data/05.txt", "r") as f:
        pt1 = 0
        pt2 = 0
        ranges = []
        adding_ranges = True
        for line in f:
            if line == "\n":
                adding_ranges = False
                continue
            if adding_ranges is True:
                start, _, end = line.strip("\n").partition("-")
                ranges.append([int(start), int(end)])
            else:
                for rng in ranges:
                    if int(line.strip("\n")) <= rng[1] and int(line) >= rng[0]:
                        pt1 += 1
                        break
        return pt1, pt2


if __name__ == "__main__":
    print(f"{run()=} ")
