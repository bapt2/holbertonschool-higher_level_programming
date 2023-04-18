#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
let count = 0;

request(id, (err, response, body) => {
  if (!err) {
    const Body = JSON.parse(body);
    const result = Body.results;
    for (let i = 0; i < result.length; i++) {
      const characters = result[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count += 1;
        }
      }
    }
  }
  console.log(count);
});
