from pathlib import Path


def pt1():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        result = 0
        for line in f:
            line = line.strip("\n")
            start_idx: int = 0
            first: int = 0
            for idx, digit in enumerate(line[:-1]):
                if int(digit) > first:
                    first = int(digit)
                    start_idx = idx + 1
            result += first * 10
            result += (
                int(line[-1])
                if start_idx == len(line) - 1
                else max(*[int(digit) for digit in line[start_idx:]])
            )
        return result


def pt2():
    with open(f"{Path(__file__).parent}/data/03.txt", "r") as f:
        result = 0
        for line in f:
            line = line.strip("\n")
            start_idx: int = 0
            slice_end = -11
            while slice_end < 0:
                cur_idx: int = 0
                cur_digit = 0
                for idx, digit in enumerate(line[start_idx:slice_end]):
                    if int(digit) > cur_digit:
                        cur_digit = int(digit)
                        cur_idx = idx + start_idx
                result += 10 ** (-slice_end) * cur_digit
                slice_end += 1
                start_idx = cur_idx + 1
            result += (
                int(line[-1])
                if start_idx == len(line) - 1
                else max(*[int(digit) for digit in line[start_idx:]])
            )
        return result


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
