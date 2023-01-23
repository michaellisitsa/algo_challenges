#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#  3. maxNum: Largest unique integer that can be used.


def powerSum(X: int, N: int, maxNum: int | None = None) -> int:
    # The largest unique integer can be no larger.
    nthRoot: float = X ** (1 / N)

    i: int = int(nthRoot)

    # ensure only powers of unique numbers can be used.
    # i.e. numbers above maxNum have been used already.
    if maxNum is not None:
        i = min(i, maxNum)

    sum: int = 0

    # The while loop necessary to check each value less than the nthRoot / maxNum. e.g.
    # - 100 - 10^2
    # - 100 - 9^2
    # - 100 - 8^2

    while i > 0:
        # Only the first iteration could lead to power sum.
        # i.e. when nthRoot is an integer, then by definition X - i**N == 0
        # however, if we're on subsequent iterations, i < nthRoot
        # so X - i**N > 0.
        if i == int(nthRoot) and nthRoot.is_integer():
            sum += 1
        elif i != 1:
            # If i is down to 1, then X - 1^2 > 0,
            # else the above condition would've triggered
            # as nthRoot & X would've had to be 1.
            sum += powerSum(X - i**N, N, maxNum=i - 1)
        i -= 1
    return sum


print(powerSum(100, 2))
