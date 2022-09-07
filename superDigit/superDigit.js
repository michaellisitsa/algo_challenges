// https://www.hackerrank.com/challenges/recursive-digit-sum/problem
/*
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 * string n: a string representation of an integer
 * int k: the times to concatenate  to make
 */

function superDigit(n, k) {
  const sumDigits = (string) =>
    Array.from(string.toString()).reduce(
      (accum, current) => parseInt(current) + accum,
      0
    );
  function recursiveSuperDigit(s) {
    const currentSuperDigit = sumDigits(s);
    return currentSuperDigit.toString().length > 1
      ? recursiveSuperDigit(currentSuperDigit)
      : currentSuperDigit;
  }
  return recursiveSuperDigit(sumDigits(n) * k);
}
console.log(superDigit("912", 8));
