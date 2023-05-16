from queue import LifoQueue

# Complete the 'twoStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER maxSum
#  2. INTEGER_ARRAY a
#  3. INTEGER_ARRAY b
#


def twoStacks(maxSum: int, a: list[int], b: list[int]):
    # a_stack = LifoQueue(maxsize=len(a))
    # b_stack = LifoQueue(maxsize=len(b))

    # Dig down as far as possible in a, until  maxSum is exceeded.
    a_depth = 0
    a_sum = 0
    a_copy = a.copy()
    while a_sum <= maxSum:
        a_depth += 1
        a_sum += a_copy.pop(0)

    a_depth = a_depth - 1 if a_depth > 0 else 0
    return a_depth
    # Record how far you dug, say depth
    # Now dig depth-1, and start pulling from pile b.
    # Record the max score once you exceed maxSum
    # Now dig depth-2, and start pulling from pile b.
    # rinse and repeat.


print(twoStacks(10, [1, 2, 3, 5, 6, 7, 8], [1, 2, 3]))
