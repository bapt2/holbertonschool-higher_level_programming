#!/usr/bin/node

const x = process.argv[2];
const sentence = 'C is fun';
if (parseInt(x, 10)) {
  for (let i = 0; i < x; i++) {
    console.log(sentence);
  }
} else {
  console.log('Missing number of occurrences');
}
