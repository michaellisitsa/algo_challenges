const DirectChaining = require('./directChaining');

describe('DirectChaining', () => {
  
test('adding 2 items with the same hash', () => {
  
  const table = new DirectChaining(3);
  table.insertValue(3);
  table.insertValue(6);
  expect(table.hashTable).toEqual([[3,6]]);
});
});