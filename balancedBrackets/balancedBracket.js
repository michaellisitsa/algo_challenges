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

  deleteHead() {
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
      if (char !== stack.tail?.value) {
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

  const t = parseInt(readLine().trim(), 10);
  // UNCOMMENT IF READING FROM FILE
  // const t = 1;

  for (let tItr = 0; tItr < t; tItr++) {
    const s = readLine();
    // UNCOMMENT IF READING FROM FILE
    // const s = fs.readFileSync(
    //   `/Users/michaellisitsa/Documents/learning/algo_challenges/balancedBrackets/long_sample.txt`,
    //   "utf8"
    // );

    const result = isBalanced(s);

    ws.write(result + "\n");
    console.log(s, " is ", result === "YES" ? "balanced" : "unbalanced");
  }

  ws.end();
}
