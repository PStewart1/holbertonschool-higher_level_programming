#!/usr/bin/node

const args = process.argv.slice(2).map(num => parseInt(num));
if (args.length <= 1) {
  console.log(0);
} else {
  // args.sort();
  const num = args.sort().slice(-2)[0];
  console.log(num);
}
