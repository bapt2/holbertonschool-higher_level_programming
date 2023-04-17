#!/usr/bin/node

const request = require('request');
const argv = process.argv[2];

request({
    url: 'https://swapi-api.hbtn.io/api/films/${argv}',
    json: true
}, (err, responce, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.title);
});
