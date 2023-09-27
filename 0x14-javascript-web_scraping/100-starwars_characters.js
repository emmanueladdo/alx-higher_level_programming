#!/usr/bin/node
/**
 *scripts computes the number task
 *
 */

const request = require('request');

const ID = process.argv[2]; // Get the API URL from command line arguments

const urlAPi = 'https://swapi-api.hbtn.io/api/films/'+ `${ID}`;
if (!ID) {
  console.error('Usage: ./100-starwars_characters.js <ID>');
  process.exit(1);
}

request(url, (error, response, body) => {
    if (error) console.log(error);
    else {
      const characters = JSON.parse(body).characters;
      characters.forEach((character) => {
        request(character, (error, response, body) => {
          if (error) console.log(error);
          else console.log(JSON.parse(body).name);
        });
      });
    }
  });