#!/usr/bin/node
const a = parseInt(process.argv[2]);

if (isNaN(a) || a < 0) console.log('NaN');
else if (a === 0 || a === 1) console.log(1);
else {
  let total = 1;
  let num = 1;
  while (num <= a) {
    total *= num;
    num++;
  }
  console.log(total);
}
