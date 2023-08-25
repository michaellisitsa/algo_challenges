const DirectChaining = require('./directChaining');

describe('DirectChaining', () => {
  test('adding 2 items with the same hash', () => {
    const table = new DirectChaining(3);
    table.insertValue(3);
    table.insertValue(6);
    expect(table.hashTable).toEqual([[3, 6]]);
  });

  test('adding 2 items with different hashes', () => {
    const table = new DirectChaining(3);
    table.insertValue(2);
    table.insertValue(6);
    expect(table.hashTable).toEqual([[6], undefined, [2]]);
  });

  test('adding identical item twice only adds once', () => {
    const table = new DirectChaining(3);
    table.insertValue(3);
    table.insertValue(3);
    expect(table.hashTable).toEqual([[3]]);
  });

  test('delete item where key becomes empty', () => {
    const table = new DirectChaining(3);
    table.insertValue(6);
    table.insertValue(3);
    table.deleteValue(3);
    expect(table.hashTable).toEqual([[6]]);
  });
});