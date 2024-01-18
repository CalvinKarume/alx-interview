#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node 0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error || response.statusCode !== 200) {
    console.error('Error:', error || response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const { characters } = movieData;

  if (characters.length === 0) {
    console.log('No characters found for this movie.');
    return;
  }

  function printCharacters(index) {
    if (index >= characters.length) return;

    const characterUrl = characters[index];
    request(characterUrl, (characterError, characterResponse, characterBody) => {
      if (!characterError && characterResponse.statusCode === 200) {
        console.log(JSON.parse(characterBody).name);
      } else {
        console.error('Error fetching character data:', characterError || characterResponse.statusCode);
      }

      printCharacters(index + 1);
    });
  }

  printCharacters(0);
});


