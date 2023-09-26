#!/usr/bin/node
/* The script display title of starwars by ID
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const ID = process.argv[2];

const request = require('request');

if (!ID) {
  console.error('Usage: ./3-starwars_title.js <ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${ID}`;

request(apiUrl, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 200) {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
