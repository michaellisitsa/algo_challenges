function move(grid, traversers, goalX, goalY, moves) {
  // Move walker one in each orthogonal directions, stopping at walls or "X" or a number already.
  let i = 0;
  while (i < traversers.length) {
    let traverser = traversers[i];
    let position =
      traverser.direction === "up" || traverser.direction === "down"
        ? traverser.y
        : traverser.x;
    function currentLocationIndex() {
      if (traverser.direction === "up" || traverser.direction === "down") {
        return [traverser.x, position];
      } else {
        return [position, traverser.y];
      }
    }
    function nextLocationIndex() {
      switch (traverser.direction) {
        case "up":
          return [traverser.x, position - 1];
        case "down":
          return [traverser.x, position + 1];
        case "left":
          return [position - 1, traverser.y];
        case "right":
          return [position + 1, traverser.y];
      }
    }
    const nextLocationValue = () => {
      try {
        return grid[nextLocationIndex()[0]][nextLocationIndex()[1]];
      } catch (e) {
        return "X";
      }
    };
    // const location = nextLocationValue();
    // const value = nextLocationValue();
    // const index = nextLocationIndex();
    // - If moved 1 place, mark set end location with 1.
    // - If move 2 places, mark this and traversed location as 1.
    const positiveDirection =
      traverser.direction === "right" || traverser.direction === "down";
    while (
      (positiveDirection ? position < grid.length - 1 : position > 0) &&
      nextLocationValue() === "." &&
      nextLocationIndex() !== [goalX, goalY] &&
      isNaN(nextLocationValue())
    ) {
      grid[nextLocationIndex()[0]][nextLocationIndex()[1]] = moves;
      position = positiveDirection ? position + 1 : position - 1;
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
      traverser.x = currentLocation[0];
      traverser.y = currentLocation[1];
      i++;
    }

    // If reached destination, return from function.
    if (currentLocation[0] === goalX && currentLocation[1] === goalY) {
      return grid[currentLocation[0]][currentLocation[1]];
    }
  }
  let newTraversers = [];
  traversers.forEach((traverser) => {
    const location = {
      x: traverser.x,
      y: traverser.y,
    };
    if (traverser.direction === "up" || traverser.direction === "down") {
      newTraversers.push({
        ...location,
        direction: "left",
      });
      newTraversers.push({
        ...location,
        direction: "right",
      });
    } else {
      newTraversers.push({
        ...location,
        direction: "up",
      });
      newTraversers.push({
        ...location,
        direction: "down",
      });
    }
  });
  return move(grid, newTraversers, goalX, goalY, moves + 1);
}

function minimumMoves(grid, startX, startY, goalX, goalY) {
  // Mark current location as "X"
  const newGrid = grid.map((row) => row.split(""));
  newGrid[startX][startY] = 0;
  // Have array of 2 walkers, each having a:
  const traversers = [
    {
      // - current position of walker
      x: startX,
      y: startY,
      // - direction of next move
      direction: "up",
    },
    {
      x: startX,
      y: startY,
      direction: "down",
    },
    {
      x: startX,
      y: startY,
      direction: "left",
    },
    {
      x: startX,
      y: startY,
      direction: "right",
    },
  ];

  return move(newGrid, traversers, goalX, goalY, 1);
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

console.log("answer", minimumMoves(grid, 0, 0, 2, 0));
