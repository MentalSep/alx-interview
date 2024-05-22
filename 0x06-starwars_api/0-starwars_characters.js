#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Response status code: ${response.statusCode} From using the movie ID: ${movieId}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characterUrls = filmData.characters;
  const characterNames = new Array(characterUrls.length);
  let completedRequests = 0;

  characterUrls.forEach((characterUrl, index) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error(`Response status code: ${response.statusCode} while fetching charater data`);
        return;
      }

      const characterData = JSON.parse(body);
      characterNames[index] = characterData.name;
      completedRequests++;

      if (completedRequests === characterUrls.length) {
        characterNames.forEach(name => {
          console.log(name);
        });
      }
    });
  });
});
