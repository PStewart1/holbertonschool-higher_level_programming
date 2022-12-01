#!/usr/bin/node

const num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= num; i++) {
    console.log('C is fun');
  }
}
