process.stdin.resume();
process.stdin.setEncoding("ascii");
process.stdin.on("data", function (input) {
  main();
  console.log(
    `Func Source Length ${main.toString().replace(/\s/g, "").length}`
  );
});

function main() {
  for (i = 1; i <= 100; i++) {
    if (i % 15 === 0) {
      console.log("FizzBuzz");
    } else if (i % 3 === 0) {
      console.log("Fizz");
    } else if (i % 5 === 0) {
      console.log("Buzz");
    } else {
      console.log(i);
    }
  }
}
