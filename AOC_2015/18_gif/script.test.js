import getNeighbourCount from "./utils/getNeighbourCount";

test("top left corner all on", () => {
  const data = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  expect(getNeighbourCount(0, data)).toBe(3);
});

test("top left corner all top row on", () => {
  const data = [1, 1, 1, 0, 0, 0, 0, 0, 0];
  expect(getNeighbourCount(0, data)).toBe(1);
});

test("middle value top row", () => {
  const data = [1, 1, 1, 0, 0, 0, 0, 0, 0];
  expect(getNeighbourCount(1, data)).toBe(2);
});

test("end value top row", () => {
  const data = [1, 1, 1, 0, 0, 0, 0, 0, 0];
  expect(getNeighbourCount(2, data)).toBe(1);
});
