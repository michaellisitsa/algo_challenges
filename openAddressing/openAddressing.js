class OpenAddressing {
  hashTable = [];
  constructor(hashSize = 3) {
    this.hashSize = hashSize;
    console.log("initialized class", this.hashTable);
  }
  insertValue(value) {
    const hashedIndex = this.hash(value);
    let newIndex = hashedIndex;
    while (this.hashTable[newIndex]) {
      newIndex += 1;
    }
    this.hashTable[newIndex] = value;
  }
  hash(value) {
    return value % this.hashSize;
  }
}

module.exports = OpenAddressing;
