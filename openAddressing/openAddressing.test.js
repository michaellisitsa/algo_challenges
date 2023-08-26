const OpenAddressing = require("./openAddressing");

describe("openAddressing", () => {
  test("it stores hash table", () => {
    const table = new OpenAddressing(3);
    expect(table.hashTable).toEqual([]);
  });
  test("it stores key at hash value if not filled", () => {
    const table = new OpenAddressing(3);
    table.insertValue(3);
    expect(table.hashTable).toEqual([3]);
  });
  test("it stores key at next free spot if hash value filled", () => {
    const table = new OpenAddressing(3);
    table.insertValue(3);
    table.insertValue(6);
    expect(table.hashTable).toEqual([3, 6]);
  });
  test("it stores key at next free spot if hash value filled", () => {
    const table = new OpenAddressing(3);
    table.insertValue(3);
    table.insertValue(4);
    expect(table.hashTable).toEqual([3, 4]);
  });
});
