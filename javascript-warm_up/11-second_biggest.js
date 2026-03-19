#!/usr/bin/node

const arg = process.argv.slice(2);
let max = 0;
let second = 0;
let i = 1;

if (arg.length < 1) {
  console.log(0);
}
else {
  while (i < arg.length) {
    if (arg[i] > max) {
      second = max;
      max = arg[i];
    }
    if (arg[i] < max && arg[i] > second) {
      second = arg[i];
    }
    i++;
  }
  console.log(second);
}
