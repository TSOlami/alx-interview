#!/usr/bin/node

const request = require('request');

// Get the movie ID from command line argument
const movieId = process.argv[2];

// Construct the movie API endpoint URL
const movieEndpoint = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

// Function to send requests to retrieve character names
function sendRequest(characterList, index) {
  // Check if we've processed all characters
  if (characterList.length === index) {
    return;
  }

  // Send a request to retrieve character information
  request(characterList[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      // Parse and print the character's name
      console.log(JSON.parse(body).name);

      // Move on to the next character
      sendRequest(characterList, index + 1);
    }
  });
}

// Send a request to retrieve movie information
request(movieEndpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Parse the movie's character list
    const characterList = JSON.parse(body).characters;

    // Start retrieving character names
    sendRequest(characterList, 0);
  }
});
