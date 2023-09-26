#!/usr/bin/node
/* The script display title of starwars by ID
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const apiUrl = process.argv[2];

const fs = require('fs');

const contentfile = process.argv[3];

const request = require('request');

if (!apiUrl || !contentfile) {
  console.error('Usage: ./5-request_store.js <apiUrl> <Content-File>');
  process.exit(1);
}

request(apiUrl, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 200) {
    fs.writeFile(contentfile, body, 'utf-8', (error) => {
      if (error) console.log(error);
    });
  }
});
