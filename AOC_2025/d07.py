from pathlib import Path


def pt1():
    with open(f"{Path(__file__).parent}/data/07.txt", "r") as f:
        result = 0
        prev: list[str] = []
        for idx, line in enumerate(f):
            if idx == 0:
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
                # print("".join(line_lst))
        return result


num_forks = 0


def dfs(lines: list[list[str]], ray_idx: int, line_idx) -> int:
    global num_forks
    if ray_idx == 0 or ray_idx == len(lines[0]) - 1:
        return 0
    if len(lines) - line_idx > 0:
        if lines[line_idx][ray_idx] == ".":
            return dfs(lines, ray_idx, line_idx + 1)
        else:
            # Has '^'
            # this
            # . | . . . # exclude
            # . ^ . . .
            # | . . . .
            # and
            # . | . . . # exclude
            # . ^ . . .
            # . . | . .
            num_forks += 1
            return dfs(lines, ray_idx - 1, line_idx + 1) + dfs(
                lines, ray_idx + 1, line_idx + 1
            )
    # No lines left
    return 0


def pt2():
    lines: list[list[str]] = []
    global num_forks
    with open(f"{Path(__file__).parent}/data/07.txt", "r") as f:
        ray_idx = 0
        for idx, line in enumerate(f):
            if idx == 0:
                # We don't need to append first line, only note its location
                line = line.replace("S", "|")
                ray_idx = line.index("|")
            else:
                lines.append(list(line.rstrip()))

        # This is just for testing.
        # Increases exponentially, too slow beyond 85
        for i in range(69, 80, 2):
            num_forks = 1
            dfs(lines[:i], ray_idx, 0)
            print(f"rows:{i} count:{num_forks=}")


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
    # print(num_visits)
