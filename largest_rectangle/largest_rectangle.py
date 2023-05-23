# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h: list[int]):
    # current_max = 0
    current_start_indexes: list[int] = []
    for current_height_idx, current_height in enumerate(h):
        current_start_indexes.extend(
            ascending_array_of_value(
                previous_idx=len(current_start_indexes),
                new_idx=current_height,
                value=current_height_idx,
            )
        )
        
        print(current_start_indexes)


# Shouldn't need to know about modifying the outside world
def ascending_array_of_value(previous_idx: int, new_idx: int, value: int) -> list[int]:
    if new_idx > previous_idx:
        return [value] * (new_idx - previous_idx)
    return []


