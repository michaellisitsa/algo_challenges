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

const reverseRange = (start, end) => {
  let output = [];
  if (typeof end === "undefined") {
    end = start;
    start = 0;
  }
  for (let i = start; i <= end; i += 1) {
    output.push(i);
  }
  return output.reverse();
};

function almostSorted(arr) {
  const sortedArr = [...arr].sort((a, b) => a - b);
  const unorderedIndexes = compareDifferentArrays(arr, sortedArr);
  const unorderedValues = unorderedIndexes.map((idx) => arr[idx]);
  console.log("unordered values:", unorderedValues);
  if (unorderedIndexes.length === 0) {
    return "yes";
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
  } else if (
    unorderedIndexes.length > 2 &&
    compareDifferentArrays(
      unorderedValues,
      reverseRange(Math.min(...unorderedValues), Math.max(...unorderedValues))
    ).length === 0
  ) {
    let reversedArr = [...arr];
    reversedArr.splice(
      unorderedIndexes[0],
      unorderedIndexes.length,
      ...unorderedValues.reverse()
    );
    if (compareDifferentArrays(reversedArr, sortedArr).length === 0) {
      return `yes\nreverse ${unorderedIndexes[0]} ${
        unorderedIndexes[unorderedIndexes.length - 1]
      }`;
    }
    return "no";
  }
}

/*

*/

// const returned = almostSorted([4, 2]);
const returned = almostSorted([4, 3, 2, 1, 5]);
// const returned = almostSorted([7, 2, 3, 4, 5, 1]);
console.log("returned", returned);
