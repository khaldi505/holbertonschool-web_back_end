const http = require('http');

const hostname = '127.0.0.1';
const port = 1245;
const countStudents = require('./3-read_file_async');

const filePath = process.argv[2];

const promise = countStudents(filePath);

const app = http.createServer((req, res) => {
  if (req.url === '/students') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    promise.then((data) => {
      res.end(`This is the list of our students\n${data}`);
    }).catch(() => { res.end('This is the list of our students\nCannot load the database'); });
  } else if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  }
});

module.exports = app.listen(port, hostname);
