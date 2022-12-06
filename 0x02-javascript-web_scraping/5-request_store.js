#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
const options = { json: true };
request(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, body, 'utf8', function (error) {
      if (error) { console.log(error); }
    });
  }
});
