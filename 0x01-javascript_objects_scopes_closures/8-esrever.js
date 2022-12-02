#!/usr/bin/node

exports.esrever = function (list) {
  const output = [];
  for (let i = list.length - 1; i >= 0; i--) {
    output.push(list[i]);
  }
  return output;
};
