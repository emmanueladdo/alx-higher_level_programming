#!/usr/bin/node

/**
 * Prints the number of arguments already printed
 * And the argument value.
 */

let numArgs = 0;
exports.logMe = function (item) {
  console.log(numArgs + ': ' + item);
  numArgs++;
};
