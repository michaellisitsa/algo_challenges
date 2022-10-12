/*
 * Complete the 'migratoryBirds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

arr = [1, 1, 5, 5, 2, 3];

function migratoryBirds(arr) {
  const countArr = arr.reduce((accum, current) => {
    return {
      ...accum,
      [parseInt(current)]: parseInt(accum[current]) + 1 || 1,
    };
  }, {});
  const max = Object.values(countArr).reduce((accum, current) =>
    accum < current ? current : accum
  );
  return Object.entries(countArr).reduce((accum, current) => {
    if (current[1] === max && current[0] < accum) {
      return current[0];
    } else {
      return accum;
    }
  }, 999);
}
console.log(migratoryBirds(arr));
