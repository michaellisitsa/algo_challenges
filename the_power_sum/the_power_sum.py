#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def powerSum(X: int, N: int) -> int:
    # Get Nth Root of X e.g. X**(1/N)
    nthRoot: float = X ** (1 / N)
    # print(nthRoot.is_integer())
    if nthRoot.is_integer():
        print("success", nthRoot)
        return 1
    else:
        # Floor the nthRoot
        nthRootFloor: int = int(nthRoot)
        XLVL1: int = X - (nthRootFloor - 1) ** N
        return 0 + powerSum(XLVL1, N)


powerSum(13, 2)
