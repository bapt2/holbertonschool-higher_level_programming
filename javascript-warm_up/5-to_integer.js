#!/usr/bin/node

const a = process.argv[2];
if (parseInt(a, 10)) {
  console.log('My number: ' + a);
} else {
  console.log('Not a number');
}
