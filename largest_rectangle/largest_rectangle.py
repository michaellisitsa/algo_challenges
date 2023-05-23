# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#


def largestRectangle(h: list[int]):
    max_area: int = 0
    start_indices: list[int] = []
    for current_height_idx, current_height in enumerate(h):
        start_indices.extend(
            ascending_array_of_value(
                previous_idx=len(start_indices),
                new_idx=current_height,
                value=current_height_idx,
            )
        )
        if current_height < len(start_indices):
            # The next building is shorter, so need to sum up all the taller levels.
            print("Index: ", current_height_idx)
            print("current Height", current_height)
        
        print(current_start_indexes)
            for height in reversed(range(current_height + 1, len(start_indices) + 1)):
                area = height * (current_height_idx - start_indices[height - 1])
                print(
                    "For storey",
                    height,
                    "of width ",
                    (current_height_idx - start_indices[height - 1]),
                    "the area is: ",
                    area,
                )
                max_area = max(area, max_area)
                # We no longer need to track that height as we've saved it if
                # was the maximum.
                start_indices.pop()
    # For the last iteration, we get the sums of the remaining values:
    for height in range(1, len(start_indices) + 1):
        end_position = len(h)
        area = height * (end_position - start_indices[height - 1])
        max_area = max(area, max_area)

    return max_area


# Shouldn't need to know about modifying the outside world
def ascending_array_of_value(previous_idx: int, new_idx: int, value: int) -> list[int]:
    if new_idx > previous_idx:
        return [value] * (new_idx - previous_idx)
    return []


