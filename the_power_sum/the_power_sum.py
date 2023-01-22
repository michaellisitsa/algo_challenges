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
    if int(nthRoot) == 1:
        return 0
    elif nthRoot.is_integer():
        # print("success", nthRoot)
        # print("new X: ", X - (int(nthRoot) - 1) ** N)
        return 1 + powerSum(
            X - (int(nthRoot) - 1) ** N,
            N,
        )
    else:
        # Floor the nthRoot
        nthRootFloor: int = int(nthRoot)
        XLVL1: int = X - nthRootFloor**N
        rootXLVL1 = XLVL1 ** (1 / N)
        recurse = X - int(nthRoot) ** N

        if rootXLVL1 >= nthRootFloor:
            return 0 + powerSum(
                recurse,
                N,
            )
        else:
            return 0 + powerSum(XLVL1, N)


print(powerSum(100, 2))
