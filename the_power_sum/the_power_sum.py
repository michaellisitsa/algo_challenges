#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def powerSum(X: int, N: int):
    # Get Nth Root of X e.g. X**(1/N)
    nthRoot: float = X**(1/N)
    # print(nthRoot.is_integer())
    if nthRoot.is_integer():
        print("success", nthRoot)
        return 1
    else:
        # Floor the nthRoot
        nthRootFloor: int = int(nthRoot)
        XLVL1: int = X - (nthRootFloor-1)**N
        print(f"XLVL1: {XLVL1}")
        nthRootLVL1: float = XLVL1**(1/N)
        if nthRootLVL1.is_integer():
            print("success lvl1", nthRootLVL1)
            return 1
        else:
            print("not success lvl1")
            return 0


powerSum(13,2)