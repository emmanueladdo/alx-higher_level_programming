#!/usr/bin/node
/* The file reads and prints a file
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const fs = require('fs');

const filePath = process.argv[2];

if (!filePath) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

fs.readFile(filePath, 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
  } else {
    console.log(data);
  }
});
