function minimumMoves(grid, startX, startY, goalX, goalY) {
  // Mark current location as "X"
  const newGrid = grid.map((row) => row.split(""));
  newGrid[startY][startX] = 0;
  // Have array of 2 walkers, each having a:
  const traversers = [
    {
      // - current position of walker
      x: startX,
      y: startY,
      // - axes of next move
      direction: "vertical",
    },
    {
      x: startX,
      y: startY,
      direction: "horizontal",
    },
  ];
  // Move walker one in each orthogonal directions, stopping at walls or "X" or a number already.
  let i = 0;
  while (i < traversers.length) {
    let traverser = traversers[i];
    let position =
      traverser.direction === "vertical" ? traverser.y : traverser.x;
    function currentLocationIndex() {
      if (traverser.direction === "vertical") {
        return [traverser.x, position];
      } else {
        return [position, traverser.y];
      }
    }
    function nextLocationIndex() {
      if (traverser.direction === "vertical") {
        return [traverser.x, position + 1];
      } else {
        return [position + 1, traverser.y];
      }
    }
    const nextLocationValue = () =>
      newGrid[nextLocationIndex()[1]][nextLocationIndex()[0]];
    // const value = nextLocationValue();
    // const index = nextLocationIndex();
    // - If moved 1 place, mark set end location with 1.
    // - If move 2 places, mark this and traversed location as 1.
    while (
      position < grid.length - 1 &&
      nextLocationValue() === "." &&
      nextLocationIndex() !== [goalX, goalY] &&
      isNaN(nextLocationValue())
    ) {
      if (traverser.direction === "vertical") {
        newGrid[position + 1][traverser.y] = 1;
      } else {
        newGrid[traverser.x][position + 1] = 1;
      }
      position += 1;
    }
    const currentLocation = currentLocationIndex();
    // - If moved 0 places, delete walker.
    if (
      currentLocation[0] === traverser.x &&
      currentLocation[1] === traverser.y
    ) {
      traversers.splice(i, 1);
    } else {
      // Go to next traverser
      i++;
    }

    // If reached destination, return from function.
    if (currentLocation[0] === goalX && currentLocation[1] === goalY) {
      return newGrid[currentLocation[1]][currentLocation[0]];
    }
  }
  // Check if the goal is marked with a 1. return.
  // Set the current position and axes of next move
  // For each of the walkers, move in each of the orthogonal directions
  // Place a number on each direction.
  // - If moved 0 places, don't save walker.
  // - If moved 1 place, mark set end location with 2. Add walker to array
  // - If move 2 places, mark this and traversed location as 2. Add walker to array
  // Then delete the current walker.
  //
}

const grid = [".X.", ".X.", "..."];

console.log("answer", minimumMoves(grid, 0, 0, 0, 2));
