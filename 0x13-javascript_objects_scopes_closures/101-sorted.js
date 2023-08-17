#!/usr/bin/node

/**
 * Imports a dict of occurrences by user id
 * Computes a dict of user ids by occurrence.
 * In the new dictionary:
 * A key is a number of occurrences
 * A value is the list of user ids
 */

const dict = require('./101-data.js').dict;
const newdict = {};
for (const key in dict) {
  if (newdict[dict[key]] === undefined) {
    newdict[dict[key]] = [key];
  } else {
    newdict[dict[key]].push(key);
  }
}
console.log(newdict);
