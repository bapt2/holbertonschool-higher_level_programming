#!/usr/bin/node

const fs = require('fs');
const argv = process.argv[2];
const data = process.argv[3];

fs.writeFile(argv, data, 'utf-8', (err, data) => {
  if (err);
});
