#!/usr/bin/node

const { argv } = require('process');
const list = [];
if (argv[2] === undefined) {
  console.log('0');
} else {
  let count = 0;
  for (let i = 2; argv[i]; i++) {
    const number = parseInt(argv[i]);
    list.push(number);
    count += 1;
  } if (count === 1) {
    console.log(0);
  } else {
    list.sort(function (a, b) {
      return a - b;
    });
    console.log(list[count - 2]);
  }
}
