#!/usr/bin/node
 
const x = parseInt(process.argv[2], 10);
if (x) {
  for (let i = 0; i < x; i++) {
    console.log('X'.repeat(x));
  }
} else {
  console.log('Missing size');
}
