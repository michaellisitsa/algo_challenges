function recursiveSort(n, arr, valueToSort) {
  let newArr = [...arr];
  if (valueToSort < arr[n - 2]) {
    newArr.splice(n - 1, 1, newArr[n - 2]);
    console.log(newArr.join(" "));
    return recursiveSort(n - 1, newArr, valueToSort);
  } else {
    newArr.splice(n - 1, 1, valueToSort);
    console.log(newArr.join(" "));
  }
}

/*
 * Complete the 'insertionSort1' function below.
 *
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY arr
 */

function insertionSort1(n, arr) {
  const unsortedVal = arr[n - 1];
  recursiveSort(n, arr, unsortedVal);
}

insertionSort1(5, [1, 2, 4, 5, 3]);
