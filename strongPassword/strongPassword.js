// Hackerrank challenge
// https://www.hackerrank.com/challenges/strong-password/problem?isFullScreen=true

const numbers = "0123456789";
const lowercase = "abcdefghijklmnopqrstuvwxyz";
const uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const specialCharacters = "!@#$%^&*()-+";
const counts = {
  length: 6,
  numbers: 1,
  lowercase: 1,
  uppercase: 1,
  specialCharacters: 1,
};

function categorise(char) {
  if (numbers.includes(char)) {
    return "numbers";
  } else if (lowercase.includes(char)) {
    return "lowercase";
  } else if (uppercase.includes(char)) {
    return "uppercase";
  } else if (specialCharacters.includes(char)) {
    return "specialCharacters";
  }
}

/* INPUT
 * int n: the length of the password
 * string password: the password to test
 * RETURN
 * int: the minimum number of characters to add */
function minimumNumber(n, password) {
  // Return the minimum number of characters to make the password strong
  const remainders = Array.from(password).reduce((accum, current) => {
    const charType = categorise(current);
    return {
      ...accum,
      length: accum.length > 0 ? accum.length - 1 : accum.length,
      [charType]: accum[charType] > 0 ? accum[charType] - 1 : accum[charType],
    };
  }, counts);

  const charRemaining =
    remainders.numbers +
    remainders.lowercase +
    remainders.uppercase +
    remainders.specialCharacters;

  return remainders.length > charRemaining ? remainders.length : charRemaining;
}
