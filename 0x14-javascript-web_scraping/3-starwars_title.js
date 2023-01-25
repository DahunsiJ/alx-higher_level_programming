#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}`;
request(url, (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('An error occured. Status code: ' + res.statusCode);
  }
});
