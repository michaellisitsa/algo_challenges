# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h: list[int]):
    # current_max = 0
    current_start_indexes: list[int] = []
    for current_height_idx, current_height in enumerate(h):
        if current_height >= len(current_start_indexes):
            # for _ in range(len(current_start_indexes), current_height):
            # current_start_indexes.append(current_height_idx)
            current_start_indexes.extend(
                current_height_idx
                for _ in range(len(current_start_indexes), current_height)
            )
        print(current_start_indexes)
