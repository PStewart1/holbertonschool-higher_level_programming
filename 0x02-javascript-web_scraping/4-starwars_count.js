#!/usr/bin/node

const request = require('request');
const id = '18';
const url = process.argv[2];
const options = { json: true };
request(url, options, (err, res, body) => {
  if (err) {
    console.log(err);
  }
  let result = [];
  body.results.forEach(movie => {
    result.push(movie.characters.filter(link => link.includes(id)));
  });
  result = result.filter(list => list.length > 0);
  console.log(result.length);
});
