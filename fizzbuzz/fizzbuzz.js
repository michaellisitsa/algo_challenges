process.stdin.resume();
process.stdin.setEncoding("ascii");
process.stdin.on("data", function (input) {
  main();
  console.log(
    `Func Source Length ${main.toString().replace(/\s/g, "").length}`
  );
});

function mainStart() {
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

// function main() {
//   Array(100)
//     .fill()
//     .forEach((_, i) => {
//         a="fizz";b="buzz";
//      v = m => (i+1) % m;
//       console.log(
//         !v(15)
//           ? a+b
//           : !v(3)
//           ? a
//           : !v(5)
//           ? b
//           : i+1
//       );
//     });
// }

//126
// function main() {
//   Array(100)
//     .fill()
//     .forEach((_, i) =>
//       console.log(
//         !((i + 1) % 15)
//           ? "fizzbuzz"
//           : !((i + 1) % 3)
//           ? "fizz"
//           : !((i + 1) % 5)
//           ? "buzz"
//           : i + 1
//       )
//     );
// }

// 124
// function main() {
//   Array(100)
//     .fill()
//     .map((_,i) => 1 + i)
//     .forEach(a =>
//       console.log(
//         !(a % 15)
//           ? "fizzbuzz"
//           : !(a % 3)
//           ? "fizz"
//           : !(a % 5)
//           ? "buzz"
//           : a
//       )
//     );
// }

//
function main() {
  a = 1;
  while (a++ < 101) {
    console.log(
      !(a % 15) ? "fizzbuzz" : !(a % 3) ? "fizz" : !(a % 5) ? "buzz" : a
    );
}};
