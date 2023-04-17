#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(id, (err, responce, body) => {
  if (!err) {
    const Body = JSON.parse(body);
    let count = 0;
    for (const i in Body.characters) {
      if (i === 'https://swapi-api.hbtn.io/api/people/18/') {
        count += 1;
      }
    }
    console.log(count);
  }
});
