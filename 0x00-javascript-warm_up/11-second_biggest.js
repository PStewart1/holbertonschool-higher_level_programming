#!/usr/bin/node

const args = process.argv.slice(2).sort().reverse();
if (args.length <= 1) {
  console.log(0);
} else {
  for (let i = 1; i < args.length; i++) {
    if (args[i] < args[i - 1]) {
      console.log(args[i]);
      break;
    }
  }
}
