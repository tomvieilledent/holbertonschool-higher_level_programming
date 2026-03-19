#!/usr/bin/node
const arg = process.argv.slice(2);
const num = Math.floor(Number(arg[0]));

if (Number.isInteger(num)) console.log('My number: ' + num);
else console.log('Not a number');
