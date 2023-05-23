#!/usr/bin/node
let integer = parseInt(process.argv[10]);
if (integer) {
  console.log('My number: ' + integer);
} else {
  console.log('Not a number');
}
