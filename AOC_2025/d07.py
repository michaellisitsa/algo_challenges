from pathlib import Path


def pt1():
    with open(f"{Path(__file__).parent}/data/07.txt", "r") as f:
        result = 0
        prev: list[str] = []
        start_idx = 0
        for idx, line in enumerate(f):
            if idx == 0:
                start_idx = line.index("S")
                prev = list(line.rstrip().replace("S", "|"))
            else:
                line_lst = list(line.rstrip())
                for i, char in enumerate(line_lst):
                    if prev[i] == "|" and char in [".", "|"]:
                        line_lst[i] = "|"
                    elif prev[i] == "|" and char == "^":
                        if i != 0:
                            line_lst[i - 1] = "|"
                        if i != len(line_lst) - 1:
                            line_lst[i + 1] = "|"
                        result += 1
                prev = line_lst
                print("".join(line_lst))
        return result


if __name__ == "__main__":
    print(f"{pt1()=}")
