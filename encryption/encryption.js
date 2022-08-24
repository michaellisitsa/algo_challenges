function encryption(s) {
  // Write your code here
  const str = s.replaceAll(" ", "");
  const sqrt = Math.sqrt(str.length);
  const cols = Math.ceil(sqrt);
  const rows =
    Math.floor(sqrt) * Math.ceil(sqrt) < str.length
      ? Math.ceil(sqrt)
      : Math.floor(sqrt);
  let out = "";
  const emptySpaces = cols * rows - str.length;
  for (let colIdx = 0; colIdx < cols; colIdx += 1) {
    out = colIdx > 0 ? out + " " : out;
    for (let rowIdx = 0; rowIdx < rows; rowIdx += 1) {
      // If the matrix isn't filled to the end, skip this iteration
      if (rowIdx == rows - 1 && colIdx + emptySpaces >= cols) {
        continue;
      }
      out = out + Array.from(str)[cols * rowIdx + colIdx];
    }
  }
  return out;
}

console.log(encryption("cats dog"));
