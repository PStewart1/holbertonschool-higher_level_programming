#!/usr/bin/node
const Square1 = require('./5-square');

module.exports = class Square extends Square1 {
  charPrint (c) {
    let x = 'X';
    if (c) {
      x = c;
    }
    for (let j = 1; j <= this.height; j++) {
      console.log(x.repeat(this.height));
    }
  }
};
