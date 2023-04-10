#!/usr/bin/node

let a = process.argv[2];
let b = process.argv[3];

if (a === null) {
  a = 'undefined';
} else if (b === null) {
  b = 'undefined';
} else {
  console.log(a + ' is ' + b);
}
