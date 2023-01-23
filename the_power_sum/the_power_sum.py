#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#


def powerSum(X: int, N: int, maxNum: int | None = None) -> int:
    # Get Nth Root of X e.g. X**(1/N)
    nthRoot: float = X ** (1 / N)
    # if int(nthRoot) > 1, we should kick off calculations for each of the smaller numbers.
    # return powerSum(X=result(nthRoot - 1),N)

    i: int = min(int(nthRoot), maxNum) if maxNum is not None else int(nthRoot)
    sum: int = 0
    # if nthRoot.is_integer():
    #     # print("success", nthRoot)
    #     # print("new X: ", X - (int(nthRoot) - 1) ** N)
    #     sum += 1
    while i > 0:
        if i == int(nthRoot) and nthRoot.is_integer():
            # print("success", nthRoot)
            # print("new X: ", X - (int(nthRoot) - 1) ** N)
            sum += 1
        elif i != 1:
            # print(nthRoot.is_integer())
            # Floor the nthRoot
            XLVL1: int = X - i**N
            rootXLVL1 = XLVL1 ** (1 / N)
            sum += powerSum(XLVL1, N, maxNum=i - 1)
        i -= 1
    return sum


print(powerSum(100, 2))


# def sum(a: int, b: int):
#     return a + b


# def sumArr(arr: list[int]) -> int:
#     return sum(sumArr())
