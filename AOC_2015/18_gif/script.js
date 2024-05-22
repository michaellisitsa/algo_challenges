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
      const color = value == "#" ? 255 : 0; // White for 1, black for 0

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
  data = data.trim().replace(/\r?\n|\r/g, "");
  draw(data);
  getNeighbourCount(0, Array.from(data));
}

main();
