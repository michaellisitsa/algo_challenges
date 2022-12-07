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

const splice_odd_center_from_array = (array) => {
  if (array.length % 2 > 0) {
    const midIndex = Math.floor(array.length / 2);
    return array.filter((item, index) => index !== midIndex);
  } else {
    return array;
  }
};

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
  const rangeBetweenMinAndMaxValue = reverseRange(
    Math.min(...unorderedValues),
    Math.max(...unorderedValues)
  );
  const unorderedValuesFirstHalf = unorderedValues.slice(
    0,
    unorderedValues.length / 2
  );
  const unorderedValuesSecondHalf = unorderedValues.slice(
    unorderedValues.length / 2
  );
  if (unorderedIndexes.length === 0) {
    console.log("yes");
  } else if (unorderedIndexes.length === 2) {
    const swappedArr = [...arr];
    [swappedArr[unorderedIndexes[0]], swappedArr[unorderedIndexes[1]]] = [
      swappedArr[unorderedIndexes[1]],
      swappedArr[unorderedIndexes[0]],
    ];
    if (compareDifferentArrays(sortedArr, swappedArr).length === 0) {
      console.log(
        `yes\nswap ${unorderedIndexes[0] + 1} ${unorderedIndexes[1] + 1}`
      );
    } else {
      console.log("no");
    }
  } else if (
    unorderedIndexes.length > 2 &&
    compareDifferentArrays(
      unorderedValues,
      splice_odd_center_from_array(rangeBetweenMinAndMaxValue)
    ).length === 0
  ) {
    let reversedArr = [...arr];
    if (rangeBetweenMinAndMaxValue.length % 2 > 0) {
      reversedArr.splice(
        unorderedIndexes[0],
        Math.floor(unorderedIndexes.length / 2),
        ...unorderedValuesSecondHalf.reverse()
      );
      reversedArr.splice(
        unorderedIndexes[unorderedIndexes.length / 2],
        unorderedValues.length / 2,
        ...unorderedValuesFirstHalf.reverse()
      );
    } else {
      reversedArr.splice(
        unorderedIndexes[0],
        unorderedIndexes.length,
        ...unorderedValues.reverse()
      );
    }
    if (compareDifferentArrays(reversedArr, sortedArr).length === 0) {
      console.log(
        `yes\nreverse ${unorderedIndexes[0] + 1} ${
          unorderedIndexes[unorderedIndexes.length - 1] + 1
        }`
      );
    } else {
      console.log("no");
    }
  } else {
    console.log("no");
  }
}

/*

*/

// almostSorted([4, 2]); // Expect swap 1 2
// almostSorted([3, 1, 2]); // no
// const returned = almostSorted([4, 3, 2, 1, 5]); // Expect reverse 1 4
// almostSorted([6, 1, 1, 1, 2, 1]); // expect swap 1 6
// almostSorted([6, 5, 4, 3, 2, 9]); // expect reverse 1 5
// almostSorted([1, 5, 4, 3, 2, 6]); // expect reverse 2 5
// almostSorted([1, 2, 3, 4, 5, 6]); // expect yes
// const returned = almostSorted([1, 5, 4, 3, 2, 6]); // expect reverse 2 5
// almostSorted([1, 3, 4, 10, 9, 8, 7, 6, 13, 15, 19]); // expect reverse 4 8
// almostSorted([2, 3, 5, 4]); // expect swap 3 4
almostSorted([9, 9, 9, 9]); // expect swap 3 4
