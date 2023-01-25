#!/usr/bin/node
const one = parseInt(process.argv[2]);
const two = parseInt(process.argv[3]);

function add (a, b) {
  console.log(a + b);
}
add(one, two);
