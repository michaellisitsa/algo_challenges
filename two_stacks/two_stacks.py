# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b


def sum_stack(stack: list[int]):
    sum = 0
    stack_copy = stack.copy()
    while len(stack_copy) > 0:
        sum += stack_copy.pop(0)
    return sum


def stack_depth_not_exceeding_sum(stack: list[int], max_sum: int):
    if len(stack) == 0:
        return (0, 0)
    depth = 0
    current_sum = 0
    stack_copy = stack.copy()
    while len(stack_copy) > 0 and current_sum + stack_copy[0] <= max_sum:
        depth += 1
        current_sum += stack_copy.pop(0)
    return (
        depth,
        current_sum,
    )


def twoStacks(maxSum: int, a: list[int], b: list[int]):
    # Get the max depth of the a stack only
    max_depth, _ = stack_depth_not_exceeding_sum(a, maxSum)

    # We are working with a copy of a.
    # Only the max depth is ever accessed,
    # so we throw away the rest.
    a_copy = a.copy()[:max_depth]
    # Now dig depth-1, and start pulling from pile b.
    while len(a_copy) > 0:
        # We first get the sum of the current length of the stack.
        sum = sum_stack(a_copy)

        # Start pulling from pile b
        max_depth_of_b, _ = stack_depth_not_exceeding_sum(b, maxSum - sum)

        # Store new max depth
        new_depth = len(a_copy) + max_depth_of_b
        max_depth = new_depth if new_depth > max_depth else max_depth

        # Stop iterating if we have exhausted the b list
        if max_depth_of_b == len(b):
            break
        # Once exhausted, get a with the bottom value popped off.
        a_copy.pop()

    # Check if only pulling from b stack is the high score
    max_depth_of_b, _ = stack_depth_not_exceeding_sum(b, maxSum)
    max_depth = max_depth_of_b if max_depth_of_b > max_depth else max_depth

    return max_depth


print(twoStacks(10, [1, 3, 2, 4, 6, 7, 8], [1, 2, 3]))
