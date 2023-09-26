#!/usr/bin/node
/* The script display status code
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const URLpath = process.argv[2];

const request = require('request');

if (!URLpath) {
  console.error('Usage: ./2-statuscode.js <URLpath>');
  process.exit(1);
}

request(URLpath, (err, response) => {
  if (err) { console.error(err); } else console.log(`code: ${response.statusCode}`);
});
