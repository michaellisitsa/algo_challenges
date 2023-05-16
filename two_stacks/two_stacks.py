from queue import LifoQueue

# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#


def stack_depth_not_exceeding_sum(stack: list[int], max_sum: int):
    depth = 0
    current_sum = 0
    stack_copy = stack.copy()
    while current_sum + stack_copy[0] <= max_sum:
        depth += 1
        current_sum += stack_copy.pop(0)
    return (
        depth,
        current_sum,
    )


def twoStacks(maxSum: int, a: list[int], b: list[int]):
    # Get the max depth of the a stack only
    max_depth_of_a, a_sum = stack_depth_not_exceeding_sum(a, maxSum)

    # Now dig depth-1, and start pulling from pile b.
    # Record the max score once you exceed maxSum
    # Now dig depth-2, and start pulling from pile b.
    # rinse and repeat.


print(twoStacks(10, [1, 2, 3, 5, 6, 7, 8], [1, 2, 3]))
