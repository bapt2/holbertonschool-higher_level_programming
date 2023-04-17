#!/usr/bin/node

const fs = require('fs');
const argv = process.argv.slice(2);

fs.readFile(String(argv), 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }
  console.log(data);
});
