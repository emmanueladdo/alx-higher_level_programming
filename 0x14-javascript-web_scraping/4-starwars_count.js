#!/usr/bin/node
/* The script display title of starwars by ID
 * The first arg is file path
 * The content of the file in utf-8
 * If an error occurred, print the error object
 */

const apiUrl = process.argv[2];

const request = require('request');

if (!apiUrl) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

const charID = 18;

request(apiUrl, (err, response, body) => {
  if (err) console.error(err);
  else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;

    let count = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const char in characters) {
        if (characters[char].includes(charID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
