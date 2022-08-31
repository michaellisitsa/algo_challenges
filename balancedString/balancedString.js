const string = "abcdefghhgfedecba";

function isValid(s) {
  //  For each character in string
  const byLetters = {};
  const byOccurrences = {};
  Array.from(string).forEach((char) => {
    // Retrieve from an object the number of occurrences for the current letter.
    // Increment byLetters
    byLetters[char] = byLetters[char] + 1 || 1;

    // Create byOccurrence set if doesn't exist.
    if (!byOccurrences[byLetters[char]]) {
      byOccurrences[byLetters[char]] = new Set();
    }

    // Add char to byOccurrences
    byOccurrences[byLetters[char]].add(char);

    // Delete from previous byOccurrence set
    if (byLetters[char] > 1) {
      byOccurrences[byLetters[char] - 1].delete(char);
      // Delete byOccurrence key if Set.size is zero
      if (byOccurrences[byLetters[char] - 1].size === 0) {
        delete byOccurrences[byLetters[char] - 1];
      }
    }
  });

  // Return false if > 2 keys exist
  switch (Object.keys(byOccurrences).length) {
    case 1:
      return "YES";
    case 2:
      const [[lessKey, lessSet], [moreKey, moreSet]] =
        Object.entries(byOccurrences);
      if (
        // Check that the second key set is of size 1
        moreSet.size === 1 &&
        // Check that the keys are actually next to each other
        parseInt(moreKey) === parseInt(lessKey) + 1
      ) {
        return "YES";
      } else {
        return "NO";
      }
    default:
      return "NO";
  }
}

console.log(isValid(string));
// console.log("byLetters", byLetters);
// for (const [key, set] of Object.entries(byOccurrences)) {
//   console.log("key: ", key);
//   console.log(Array.from(set.values()));
// }
