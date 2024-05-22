function matrixToFlatIndex(width) {
  return (row, col) => row * width + col;
}

export default function getNeighbourCount(currentIndex, data) {
  // We want to get the current position and check the up to 8 surrounding positions
  /*
    0 1 2
    3 4 5
    6 7 8
    */
  // First we need to calculate the indices of the surrounding positions
  const width = Math.sqrt(data.length);
  if (!Number.isInteger(width)) {
    throw new Error("Data is not square");
  }
  const getIdx = matrixToFlatIndex(width);

  const row = Math.floor(currentIndex / width);
  const col = currentIndex % width;

  if (row === 0) {
    if (col == 0) {
      // Top left corner
      return (
        data[getIdx(row, col + 1)] +
        data[getIdx(row + 1, col)] +
        data[getIdx(row + 1, col + 1)]
      );
    } else if (col == width - 1) {
      // Top right corner
      return (
        data[getIdx(row, col - 1)] +
        data[getIdx(row + 1, col - 1)] +
        data[getIdx(row + 1, col)]
      );
    } else {
      // Top row
      return (
        data[getIdx(row, col - 1)] +
        data[getIdx(row, col + 1)] +
        data[getIdx(row + 1, col - 1)] +
        data[getIdx(row + 1, col)] +
        data[getIdx(row + 1, col + 1)]
      );
    }
  }
}
