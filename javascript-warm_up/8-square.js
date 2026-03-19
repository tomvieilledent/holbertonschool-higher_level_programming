#!/usr/bin/node
const num = parseInt(process.argv[2]);

if (isNaN(num)) console.log('Missing size');
else {
  let i = 0;
  while (i < num) {
    let row = '';
    let j = 0;
    while (j < num) {
      row += 'X';
      j++;
    }
    console.log(row);
    i++;
  }
}
