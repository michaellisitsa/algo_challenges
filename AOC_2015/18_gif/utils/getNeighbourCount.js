function matrixToFlatIndex(sideLength) {
  return (row, col) => row * sideLength + col;
}

export default function getNeighbourCount(currentIndex, data) {
  // We want to get the current position and check the up to 8 surrounding positions
  /*
    0 1 2
    3 4 5
    6 7 8
    */
  // First we need to calculate the indices of the surrounding positions
  const sideLength = Math.sqrt(data.length);
  if (!Number.isInteger(sideLength)) {
    throw new Error("Data is not square");
  }
  const getIdx = matrixToFlatIndex(sideLength);

  const row = Math.floor(currentIndex / sideLength);
  const col = currentIndex % sideLength;

  if (row === 0) {
    if (col == 0) {
      // Top left corner
      return (
        data[getIdx(row, col + 1)] +
        data[getIdx(row + 1, col)] +
        data[getIdx(row + 1, col + 1)]
      );
    } else if (col == sideLength - 1) {
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
  } else if (row === sideLength - 1) {
    if (col == 0) {
      // Bottom left corner
      return (
        data[getIdx(row - 1, col)] +
        data[getIdx(row - 1, col + 1)] +
        data[getIdx(row, col + 1)]
      );
    } else if (col == sideLength - 1) {
      // Bottom right corner
      return (
        data[getIdx(row - 1, col - 1)] +
        data[getIdx(row - 1, col)] +
        data[getIdx(row, col - 1)]
      );
    } else {
      // Bottom row
      return (
        data[getIdx(row, col - 1)] +
        data[getIdx(row, col + 1)] +
        data[getIdx(row - 1, col - 1)] +
        data[getIdx(row - 1, col)] +
        data[getIdx(row - 1, col + 1)]
      );
    }
  } else {
    if (col == 0) {
      // Left column
      return (
        data[getIdx(row - 1, col)] +
        data[getIdx(row - 1, col + 1)] +
        data[getIdx(row, col + 1)] +
        data[getIdx(row + 1, col)] +
        data[getIdx(row + 1, col + 1)]
      );
    } else if (col == sideLength - 1) {
      // Right column
      return (
        data[getIdx(row - 1, col - 1)] +
        data[getIdx(row - 1, col)] +
        data[getIdx(row, col - 1)] +
        data[getIdx(row + 1, col - 1)] +
        data[getIdx(row + 1, col)]
      );
    } else {
      // Middle
      return (
        data[getIdx(row - 1, col - 1)] +
        data[getIdx(row - 1, col)] +
        data[getIdx(row - 1, col + 1)] +
        data[getIdx(row, col - 1)] +
        data[getIdx(row, col + 1)] +
        data[getIdx(row + 1, col - 1)] +
        data[getIdx(row + 1, col)] +
        data[getIdx(row + 1, col + 1)]
      );
    }
  }
}
