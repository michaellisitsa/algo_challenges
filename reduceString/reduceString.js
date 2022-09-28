function superReducedString(s) {
  let sArr = Array.from(s);
  let i = 0;
  let adjustedLength = sArr.length;
  while (i < adjustedLength - 1) {
    if (sArr[i] === sArr[i + 1]) {
      sArr.splice(i, 2);
      if (i > 0) {
        i = i - 1;
      }
      adjustedLength = adjustedLength - 2;
    } else {
      i = i + 1;
    }
  }
  if (!sArr.length) {
    return "Empty String";
  }
  return sArr.join("");
}

// console.log("Result:", superReducedString("baab"));
