#!/usr/bin/node

function factorial (x) {
  if (x > 0) {
    return (x * factorial(x - 1));
  } else {
    return 1;
  }
}
console.log(factorial(process.argv[2]));
