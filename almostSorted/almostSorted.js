/*
Input:
- Integer array
Return:
- yes (already sorted)
- no (cannot be sorted)
- yes
  reverse l r (reverse sub-segment between l & r)
- yes
  swap l r (being the 1-indices of arrays to swap)
            (choose this when both reverse & swap available)
*/

function compareDifferentArrays(firstArr, secondArr) {
  return firstArr.reduce((accum, current, idx) => {
    if (secondArr[idx] === current) {
      return accum;
    } else {
      return [...accum, idx];
    }
  }, []);
}

function almostSorted(arr) {
  const sortedArr = [...arr].sort((a, b) => a - b);
  const unorderedIndexes = compareDifferentArrays(arr, sortedArr);
  if (unorderedIndexes.length > 2) {
    return "no";
  } else if (unorderedIndexes.length === 2) {
    const swappedArr = [...arr];
    [swappedArr[unorderedIndexes[0]], swappedArr[unorderedIndexes[1]]] = [
      swappedArr[unorderedIndexes[1]],
      swappedArr[unorderedIndexes[0]],
    ];
    const unorderedIndexesOneIndexed = unorderedIndexes.map(
      (index) => index + 1
    );
    if (compareDifferentArrays(sortedArr, swappedArr).length === 0) {
      return `yes\nswap ${unorderedIndexesOneIndexed.join(" ")}`;
    }
  }
}

// const returned = almostSorted([4, 2]);
const returned = almostSorted([3, 1, 2]);
// const returned = almostSorted([7, 2, 3, 4, 5, 1]);
console.log("returned", returned);
