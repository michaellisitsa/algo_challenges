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
  function recurse(s) {
    return s.toString().length > 1 ? recurse(sumDigits(s)) : s;
  }
  return recurse(sumDigits(sumDigits(n) * k));
}
console.log(superDigit("912", 8));
