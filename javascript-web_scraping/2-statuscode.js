#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request(String(argv))
  .on('response', function (response) {
    console.log('code: ' + response.statusCode);
  })
  .on('error', function (err) {
    console.log('code: ' + err);
  });
