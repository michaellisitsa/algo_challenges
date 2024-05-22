import getNeighbourCount from "./utils/getNeighbourCount";

test("top left corner", () => {
  const data = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  expect(getNeighbourCount(0, data)).toBe(3);
});
