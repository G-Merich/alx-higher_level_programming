#!/usr/bin/node
let argc = process.argv.length;
if (argc > 3) {
  console.log('Arguments found');
} else if (argc === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
