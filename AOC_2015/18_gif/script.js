import getNeighbourCount from "./utils/getNeighbourCount.js";

// Init canvas
const width = 100;
const height = 100;
const context = document.getElementById("canvas").getContext("2d");
const imageData = context.createImageData(width, height);

async function getData() {
  try {
    const response = await fetch("./test_data.txt");
    return response.text();
  } catch (e) {
    throw new Error("Fetch failed");
  }
}

function draw(data) {
  for (let y = 0; y < height; y++) {
    for (let x = 0; x < width; x++) {
      const index = y * width + x;
      const value = data[index]; // 0 or 1

      // Each pixel is represented by 4 values (RGBA)
      const pixelIndex = index * 4;
      const color = value == 1 ? 255 : 0; // White for 1, black for 0

      imageData.data[pixelIndex] = color; // Red
      imageData.data[pixelIndex + 1] = color; // Green
      imageData.data[pixelIndex + 2] = color; // Blue
      imageData.data[pixelIndex + 3] = 255; // Alpha (fully opaque)
    }
  }
  context.putImageData(imageData, 0, 0);
}

async function main() {
  let data = await getData();
  data = Array.from(
    data
      .trim()
      .replace(/\r?\n|\r/g, "")
      .replaceAll("#", "1")
      .replaceAll(".", "0")
  ).map(Number);
  draw(data);

  let x = 0;
  let nextMap = Array(10000).fill(0);
  let previousMap = data;
  let intervalID = setInterval(function () {
    nextMap = Array(10000)
      .fill()
      .map((_, i) => {
        const neighbourCount = getNeighbourCount(i, previousMap);
        if (
          (neighbourCount === 2 || neighbourCount == 3) &&
          previousMap[i] == 1
        ) {
          return 1;
        } else if (neighbourCount === 3 && previousMap[i] == 0) {
          return 1;
        } else {
          return 0;
        }
      });
    console.log("nextMap", nextMap);
    draw(nextMap);
    previousMap = nextMap;
    if (++x === 100) {
      window.clearInterval(intervalID);
    }
  }, 200);
}

main();
