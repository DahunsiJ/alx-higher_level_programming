#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const resultIndex of results) {
      const characters = resultIndex.characters;
      for (const character of characters) {
        if (character.includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
