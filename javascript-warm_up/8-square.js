#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
let X = '';
if (x) {
  for (let i = 0; i < x; i++) {
    for (let j = 0; j < x; j++) {
      X += 'X';
    }
    X += '\n';
  }
  console.log(X);
} else {
  console.log('Missing size');
}
