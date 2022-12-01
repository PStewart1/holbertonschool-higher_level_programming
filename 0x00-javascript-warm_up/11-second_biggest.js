#!/usr/bin/node

const args = process.argv.slice(2);
let big;
let biggest = args[0];
if (args.length <= 1) {
  console.log('0');
} else {
  for (let i = 0; i <= args.length; i++) {
    if (args[i] > biggest) {
      big = biggest;
      biggest = args[i];
    }
  }
  console.log(big);
}
