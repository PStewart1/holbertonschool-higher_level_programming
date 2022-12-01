#!/usr/bin/node

const num = Number(process.argv[2]);
let x = '';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= num; i++) {
    x = '';
    for (let j = 1; j <= num; j++) {
      x = x + 'X';
    }
    console.log(x);
  }
}
