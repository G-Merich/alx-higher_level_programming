#!/usr/bin/node
const argc = process.argv.length;
if (argc > 4) {
  console.log('Arguments found');
} else if (argc === 4) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
