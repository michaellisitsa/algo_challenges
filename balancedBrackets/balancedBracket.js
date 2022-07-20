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

function isBalancedAppend(s) {
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

function isBalancedList(s) {
  let stack = [];
  for (const char of s) {
    // Use our stack to keep track of open brackets.
    if ("([{".includes(char)) {
      stack.push(char);
      continue; // Shortcut this iteration;
    }

    // If we find a close bracket and the top
    // of the stack doesn't match, then the
    // brackets aren't balanced, we can bail out.
    if (
      (char === ")" && stack.pop() !== "(") ||
      (char === "]" && stack.pop() !== "[") ||
      (char === "}" && stack.pop() !== "{")
    ) {
      return "NO";
    }
  }

  // Make sure our stack is empty and we don't
  // have any leftover brackets.
  return stack.length === 0 ? "YES" : "NO";
}

// process.env.OUTPUT_PATH = `${process.cwd()}/out.txt`
function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  // CHOOSE WHETHER TO READ FROM FILE OR FROM COMMAND LINE
  // const t = parseInt(readLine().trim(), 10); // CMDLINE
  const t = 1; // FILE

  for (let tItr = 0; tItr < t; tItr++) {
    // CHOOSE WHETHER TO READ FROM FILE OR FROM COMMAND LINE
    // const s = readLine(); // CMDLINE
    const s = fs.readFileSync(
      `${process.env.CURRENT_DIR}/deeply_nested.txt`,
      "utf8"
    ); // FILE

    // CHOOSE WHICH TEST TO RUN
    const result = isBalancedPrepend(s);
    // const result = isBalancedAppend(s);
    // const result = isBalancedList(s);

    ws.write(result + "\n");
    console.log(tItr + 1, ":", result === "YES" ? "balanced" : "unbalanced");
  }

  ws.end();
}
var result = timeit.howLong(1, main);
console.log("avg: " + result.avg);
console.log("total: " + result.total);
