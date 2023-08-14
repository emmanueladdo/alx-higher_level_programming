#!/usr/bin/node
const conArg = parseInt(process.argv[2]);
if (isNaN(conArg)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + conArg);
}
