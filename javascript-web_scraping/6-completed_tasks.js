#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, response, body) => {
  if (!err) {
    const Body = JSON.parse(body);
    let completeTask = {};
    for (let i = 0; i < Body.length; i++) {
      if (Body[i].completed === true) {
        if (completeTask[Body[i].userId] === undefined) {
          completeTask[Body[i].userId] = 0;
        }
        completeTask[Body[i].userId] += 1;
        console.log(completeTask);

      }
    }
    console.log(completeTask);
  }
});
