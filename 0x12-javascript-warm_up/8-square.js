#!/usr/bin/node
const firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < firstArg; i++) {
    let row = '';
    for (let j = 0; j < firstArg; j++) row += 'X';
    console.log(row);
  }
}
