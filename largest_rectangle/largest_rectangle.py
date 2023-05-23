def largestRectangle(h: list[int]):
    """
    The function is expected to return a LONG_INTEGER.
    The function accepts INTEGER_ARRAY h as parameter.
    """
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
            # The next building is shorter, so need to sum up all the taller levels, and see if they are larger than the maximum
            for height in reversed(range(current_height + 1, len(start_indices) + 1)):
                area = height * (current_height_idx - start_indices[height - 1])
                max_area = max(area, max_area)
                # We no longer need to track that height as we've saved it if was the maximum.
                start_indices.pop()
    # For the last iteration, we get the sums of the remaining values:
    for height in range(1, len(start_indices) + 1):
        end_position = len(h)
        area = height * (end_position - start_indices[height - 1])
        max_area = max(area, max_area)

    return max_area


def ascending_array_of_value(previous_idx: int, new_idx: int, value: int) -> list[int]:
    """Get an array of values if the new_idx is greater than the previous."""
    if new_idx > previous_idx:
        return [value] * (new_idx - previous_idx)
    return []


h_array = [10, 12, 5]
largest_area = largestRectangle(h=h_array)
print(largest_area)
