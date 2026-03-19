#!/usr/bin/node

const number = Number(process.argv[2]);

if (!Number.isInteger(number) || number <= 0) console.log('Missing number of occurrences');
else
{
    let i = 0;
    while (i < number) 
    {
    console.log('C is fun');
    i++;
    }
}
