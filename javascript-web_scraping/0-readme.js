#!/usr/bin/node

const fs = require('fs');
const argv = process.argv[2];

fs.readFile(argv, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
