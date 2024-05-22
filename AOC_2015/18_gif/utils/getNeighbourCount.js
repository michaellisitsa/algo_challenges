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

  const currentRow = Math.floor(currentIndex / width);
  const currentColumn = currentIndex % width;

  if (currentColumn === 0 && currentRow === 0) {
    // Top left corner
    return data[1] + data[width] + data[width + 1];
  } else {
    return 0;
  }
}
