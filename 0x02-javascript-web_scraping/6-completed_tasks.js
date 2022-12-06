#!/usr/bin/node

const request = require('request');
const url = process.argv[2];
const options = { json: true };
request(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  const list = {};
  body.forEach(task => {
    if (task.completed) {
      if (!(task.userId in list)) {
        list[task.userId] = 0;
      }
      list[task.userId]++;
    }
  });
  console.log(list);
});
