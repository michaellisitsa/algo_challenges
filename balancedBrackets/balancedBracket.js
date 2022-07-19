"use strict";

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
  constructor(value) {
    this.value = value;
    this.next = null;
  }

  toString = () => {
    return this.value;
  };
}

class LinkedList {
  head = null;
  tail = null;

  toArray = () => {
    let currentNode = this.head;
    if (currentNode === this.tail) {
      return [currentNode.toString()];
    }
    const linkedListArr = [];
    while (currentNode !== this.tail) {
      linkedListArr.push(currentNode.toString());
      currentNode = currentNode.next;
    }
    return linkedListArr;
  };

  peek = () => {
    if (this.head === null) {
      return null;
    }
    return this.tail.value;
  };

  pop = () => {
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
  };

  push = (value) => {
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
  };
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
      const pushedChar = stack.push(closeBrackets[openBrackets.indexOf(char)]);
    }

    if (closeBrackets.indexOf(char) !== -1) {
      if (char !== stack.peek()) {
        isBalanced = false;
        break;
      }
      stack.pop();
    }
  }
  return isBalanced && stack.head === null ? "TRUE" : "FALSE";
}
// process.env.OUTPUT_PATH = `${process.cwd()}/out.txt`
function main() {
  const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

  const t = parseInt(readLine().trim(), 10);

  for (let tItr = 0; tItr < t; tItr++) {
    const s = readLine();

    const result = isBalanced(s);

    ws.write(result + "\n");
    console.log(s, " is ", result === "TRUE" ? "balanced" : "unbalanced");
  }

  ws.end();
}
