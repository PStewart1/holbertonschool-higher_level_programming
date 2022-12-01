#!/usr/bin/node

function factorial (a) {
  const n = Number(a);
  if (isNaN(n) || n <= 1) {
    return 1;
  }
  return n * factorial(n - 1);
}

const product = factorial(process.argv[2]);
console.log(product);
