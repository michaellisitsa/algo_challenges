from pathlib import Path

def run():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        pt1 = 0
        pt2 = 0
        for line in f:
            line = line.strip("\n")
            print(f"{line}")
            print(line[:-1])
            first_idx: int = 0
            first: int = 0
            for idx, digit in enumerate(line[:-1]):
                if int(digit) > first:
                    first = int(digit)
                    first_idx = idx
            if first_idx == len(line) - 2:
                # Slice with single value is an int so cannot be iterated
                second = int(line[-1])
            else:
                second = max(*[int(digit) for digit in line[(first_idx + 1) :]])
            pt1 += first * 10 + second
        return pt1, pt2


if __name__ == "__main__":
    print(run())
