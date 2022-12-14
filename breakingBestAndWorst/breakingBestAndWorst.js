/*
 * Complete the 'breakingRecords' function below.
 *
 * The function is expected to return an INTEGER_ARRAY.
 * The function accepts INTEGER_ARRAY scores as parameter.
 */

function breakingRecords(scores) {
  let max = 0;
  let min = 0;
  scores.reduce((accum, current, currentIndex) => {
    if (currentIndex === 0) return [current, current];
    const newCount = [...accum];
    if (current > accum[0]) {
      max++;
      newCount[0] = current;
    } else if (current < accum[1]) {
      min++;
      newCount[1] = current;
    }
    return newCount;
  }, 0);
  return [max, min];
}

console.log(breakingRecords([12, 24, 10, 24]));
