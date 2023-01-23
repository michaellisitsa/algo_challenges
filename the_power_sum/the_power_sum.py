#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def powerSum(X: int, N: int, maxNum: int | None = None) -> int:
    # Get Nth Root of X
    nthRoot: float = X ** (1 / N)

    i: int = min(int(nthRoot), maxNum) if maxNum is not None else int(nthRoot)
    sum: int = 0
    while i > 0:
        if i == int(nthRoot) and nthRoot.is_integer():
            sum += 1
        elif i != 1:
            sum += powerSum(X - i**N, N, maxNum=i - 1)
        i -= 1
    return sum


print(powerSum(100, 2))
