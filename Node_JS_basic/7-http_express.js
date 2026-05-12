const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();
app.get('/', (request, response) => {
  response.send('Hello Holberton School!');
});
app.get('/students', (request, response) => {
  countStudents(database).then((result) => {
    response.send(`This is the list of our students\n${result}`);
  }).catch((error) => {
    response.send(`This is the list of our students\n${error}`);
  });
});
app.listen(1245);
module.exports = app;
