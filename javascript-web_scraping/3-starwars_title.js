#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request('https://swapi-api.hbtn.io/api/films/' + id, (err, responce, body) => {
  if (!err) {
    const Body = JSON.parse(body);
    console.log(Body.title);
  }
});
