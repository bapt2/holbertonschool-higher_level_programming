#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api = process.argv[2];
const lorispum = process.argv[3];

request(api, 'utf-8', (err, response, body) => {
  if (!err) {
    fs.writeFileSync(lorispum, body);
  }
});
