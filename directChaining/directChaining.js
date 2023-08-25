// Implement hash table with direct chaining

// Class for Direct chaining
// Store the hash table in the class
class DirectChaining {
  hashTable = [];  
  constructor (hashSize = 3) {
    this.hashSize = hashSize;
    console.log("initialized class", this.hashTable) 
  }
  
  insertValue(value) {
    const newIndex = this.hash(value);
    console.log("index", newIndex)
    // If index full, add to the existing array
    if (this.hashTable[newIndex]) {
      // Loop through each item, until you find a matching index.
      const valueIndex = this.hashTable[newIndex].indexOf(value)
      if (valueIndex === -1) {
        this.hashTable[newIndex] = [...this.hashTable[newIndex], value];
      }
    } else {
      this.hashTable[newIndex] = [value];
    }
    // If index free, create array and push to the hashTable.
    return true;
  }
  
  deleteValue(value) {
    const index = this.hash(value);
    const keyValues = this.hashTable[index];
    if (!keyValues) {
      return;
    }
    const valueIndex = keyValues.indexOf(value);
    if (valueIndex === -1) {
      return;
    } else {
      return keyValues.splice(valueIndex, 1);
    }
  }
  
  hash (value) {
    return value % this.hashSize;
//    return 10;
  }
   
}

module.exports = DirectChaining;