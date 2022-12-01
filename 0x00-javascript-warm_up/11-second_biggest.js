#!/usr/bin/node

const args = process.argv.slice(2).sort();
if (args.length <= 1) {
  console.log(0);
} else {
  console.log(args.slice(-2)[0]);
}
