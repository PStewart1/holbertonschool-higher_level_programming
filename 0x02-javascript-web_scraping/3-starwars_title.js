#!/usr/bin/node

const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
const options = { json: true };
request(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  console.log(body.title);
});
