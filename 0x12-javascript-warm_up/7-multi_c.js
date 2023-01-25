#!/usr/bin/node
let firstArg = parseInt(process.argv[2]);

if (isNaN(firstArg)) {
  console.log('Missing number of occurrences');
} else {
  while (firstArg && firstArg >= 1) {
    console.log('C is fun');
    firstArg--;
  }
}
