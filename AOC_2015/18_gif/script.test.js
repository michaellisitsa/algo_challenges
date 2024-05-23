import getNeighbourCount from "./utils/getNeighbourCount";

describe("all toggled", () => {
  const data = [1, 1, 1, 1, 1, 1, 1, 1, 1];
  test("top left corner", () => {
    expect(getNeighbourCount(0, data)).toBe(3);
  });

  test("bottom left corner", () => {
    expect(getNeighbourCount(6, data)).toBe(3);
  });

  test("bottom middle corner", () => {
    expect(getNeighbourCount(7, data)).toBe(5);
  });

  test("bottom right corner", () => {
    expect(getNeighbourCount(8, data)).toBe(3);
  });

  test("center", () => {
    expect(getNeighbourCount(4, data)).toBe(8);
  });

  test("middle row right", () => {
    expect(getNeighbourCount(5, data)).toBe(5);
  });
});

describe("top row toggled", () => {
  const data = [1, 1, 1, 0, 0, 0, 0, 0, 0];
  test("top left corner", () => {
    expect(getNeighbourCount(0, data)).toBe(1);
  });

  test("middle value top row", () => {
    expect(getNeighbourCount(1, data)).toBe(2);
  });

  test("end value top row", () => {
    expect(getNeighbourCount(2, data)).toBe(1);
  });
});
