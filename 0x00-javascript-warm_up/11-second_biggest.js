#!/usr/bin/node

const args = process.argv.slice(2);
let big = -Infinity;
let biggest = -Infinity;
if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 0; i <= args.length; i++) {
    if (args[i] > biggest) {
      big = biggest;
      biggest = args[i];
    } else if (args[i] < biggest && args[i] > big) {
      big = args[i];
    }
  }
  console.log(big);
}
