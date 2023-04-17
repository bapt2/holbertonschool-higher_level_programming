#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(id, (err, responce, body) => {
  if (!err) {
    const Body = JSON.parse(body);
    let count = 0;
    const result = Body.result;
    for (let i = 0; i < result.length; i++) {
      const characters = result[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].search('18') > 0) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
