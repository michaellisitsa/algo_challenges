"use strict";
function TimeIt() {
  var self = this;

  function howLong(iterations, testFunction) {
    var results = [];
    var total = 0;
    for (var i = 0; i < iterations; i++) {
      var start = performance.now();
      testFunction();
      var end = performance.now();
      var duration = end - start;
      results.push(duration);
      total += duration;
    }
    var result = {
      results: results,
      total: total,
      avg: total / results.length,
    };
    return result;
  }
  self.howLong = howLong;
}

var timeit = new TimeIt();

const fs = require("fs");
const dotenv = require("dotenv");
dotenv.config();

process.stdin.resume();
process.stdin.setEncoding("utf-8");

let inputString = "";
let currentLine = 0;
process.stdin.on("data", function (inputStdin) {
  inputString += inputStdin;
});

process.stdin.on("end", function () {
  inputString = inputString.split("\n");
  main();
});

function readLine() {
  return inputString[currentLine++];
}

class LinkedNode {
  constructor(value, next) {
    this.value = value;
    this.next = next;
  }

  toString() {
    return this.value;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.tail = null;
  }

  toArray() {
    let currentNode = this.head;
    if (currentNode === this.tail) {
      return [currentNode.toString()];
    }
    const linkedListArr = [];
    while (currentNode !== this.tail) {
      linkedListArr.append(currentNode.toString());
      currentNode = currentNode.next;
    }
    return linkedListArr;
  }

  deleteTail() {
    if (this.head === null) {
      return null;
    }
    let deletedNode;
    if (this.head === this.tail) {
      deletedNode = this.head;
      this.head = null;
      this.tail = null;
      return deletedNode;
    }
    let currentNode = this.head;
    while (currentNode.next !== this.tail) {
      currentNode = currentNode.next;
    }
    deletedNode = this.tail;
    if (currentNode === this.head) {
      this.head.next = null;
      this.tail = this.head;
      return;
    }
    this.tail = currentNode;
    this.tail.next = null;
    return deletedNode;
  }

  append(value) {
    const newNode = new LinkedNode(value);
    if (this.head === null) {
      this.head = newNode;
      this.tail = this.head;
      return newNode;
    }
    const prevTail = this.tail;
    this.tail = newNode;
    prevTail.next = this.tail;
    return newNode;
  }

  prepend(value) {
    const newNode = new LinkedNode(value, this.head);
    this.head = newNode;

    // If there is no tail yet let's make new node a tail.
    if (!this.tail) {
      this.tail = newNode;
    }

    return newNode;
  }

  deleteHead() {
    if (!this.head) {
      return null;
    }

    const deletedHead = this.head;

    if (this.head.next) {
      this.head = this.head.next;
    } else {
      this.head = null;
      this.tail = null;
    }

    return deletedHead;
  }

  peekHead() {
    if (this.head === null) {
      return null;
    }
    return this.head.value;
  }

  peekTail() {
    if (this.tail === null) {
      return null;
    }
    return this.tail.value;
  }
}

/*
 * Complete the 'isBalanced' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts STRING s as parameter.
 */

const openBrackets = ["[", "{", "("];
const closeBrackets = ["]", "}", ")"];

function isBalanced(s) {
  const stack = new LinkedList();
  let isBalanced = true;
  for (let char of s) {
    if (openBrackets.indexOf(char) !== -1) {
      stack.append(closeBrackets[openBrackets.indexOf(char)]);
    }

    if (closeBrackets.indexOf(char) !== -1) {
      if (char !== stack.peekTail()) {
        isBalanced = false;
        break;
      }
      stack.deleteTail();
    }
  }
  return isBalanced && stack.head === null ? "YES" : "NO";
}

function isBalancedPrepend(s) {
  const stack = new LinkedList();
  let isBalanced = true;
  for (let char of s) {
    if (openBrackets.indexOf(char) !== -1) {
      stack.prepend(closeBrackets[openBrackets.indexOf(char)]);
    }

    if (closeBrackets.indexOf(char) !== -1) {
      if (char !== stack.peekHead()) {
        isBalanced = false;
        break;
      }
      stack.deleteHead();
    }
  }
  return isBalanced && stack.head === null ? "YES" : "NO";
}

// process.env.OUTPUT_PATH = `${process.cwd()}/out.txt`
function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  // const t = parseInt(readLine().trim(), 10);
  // UNCOMMENT IF READING FROM FILE
  const t = 1;

  for (let tItr = 0; tItr < t; tItr++) {
    // const s = readLine();
    // UNCOMMENT IF READING FROM FILE
    const s = fs.readFileSync(
      `/Users/michaellisitsa/Documents/learning/algo_challenges/balancedBrackets/deeply_nested.txt`,
      "utf8"
    );

    const result = isBalancedPrepend(s);
    // const result = isBalanced(s);

    ws.write(result + "\n");
    // Console log stuffs up timing for long nested bracket test.
    // console.log(s, " is ", result === "YES" ? "balanced" : "unbalanced");
  }

  ws.end();
}
var result = timeit.howLong(1, main);
console.log("avg: " + result.avg);
console.log("total: " + result.total);
