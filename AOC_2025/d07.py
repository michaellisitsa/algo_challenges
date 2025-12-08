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
        return result


def dfs(
    lines: list[list[str]],
    ray_idx: int,
    line_idx,
    visited_nodes_count: list[list[None | int]],
) -> int:
    # The node is outside the range
    if ray_idx == 0 or ray_idx == len(lines[0]) or line_idx == len(lines):
        return 0
    # The node has already been visited
    if (current_count := visited_nodes_count[line_idx][ray_idx]) is not None:
        return current_count

    if len(lines) - line_idx > 0:
        if lines[line_idx][ray_idx] == ".":
            visited_nodes_count[line_idx][ray_idx] = dfs(
                lines, ray_idx, line_idx + 1, visited_nodes_count
            )
            return visited_nodes_count[line_idx][ray_idx]
        else:
            visited_nodes_count[line_idx][ray_idx] = (
                1
                + dfs(lines, ray_idx - 1, line_idx + 1, visited_nodes_count)
                + dfs(lines, ray_idx + 1, line_idx + 1, visited_nodes_count)
            )

            return visited_nodes_count[line_idx][ray_idx]
    # No lines left
    return 0


def pt2():
    lines: list[list[str]] = []
    with open(f"{Path(__file__).parent}/data/07.txt", "r") as f:
        ray_idx = 0
        for idx, line in enumerate(f):
            if idx == 0:
                # We don't need to append first line, only note its location
                line = line.replace("S", "|")
                ray_idx = line.index("|")
            else:
                lines.append(list(line.rstrip()))

        visited_nodes_count = [
            [None for i in range(len(lines))] for i in range(len(lines[0]))
        ]
        return dfs(lines, ray_idx, 0, visited_nodes_count) + 1


if __name__ == "__main__":
    print(f"{pt1()=} {pt2()=}")
