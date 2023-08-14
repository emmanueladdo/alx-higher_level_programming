#!/usr/bin/node
const passArg = process.argv[2];
if (passArg === undefined) {
  console.log('No argument');
} else {
  console.log(passArg);
}
