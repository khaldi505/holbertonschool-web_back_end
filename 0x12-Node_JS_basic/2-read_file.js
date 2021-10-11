const Fs = require('fs');

function countStudents(filePath) {
  try {
    let databaseFile = Fs.readFileSync(filePath, 'utf8').toString();
    databaseFile = databaseFile.split('\n');
    databaseFile.shift();
    const numOfStudents = databaseFile.length;
    const result = [`Number of students: ${numOfStudents}`, [], []];
    databaseFile.forEach((element) => {
      const resultElement = element.split(',');
      if (resultElement[3] === 'CS') {
        result[1].push(resultElement[0]);
      } else if (resultElement[3] === 'SWE') { result[2].push(resultElement[0]); }
    });

    console.log(result[0]);
    console.log(`Number of students in CS: ${result[1].length}. List: ${result[1].toString().split(',').join(', ')}`);
    console.log(`Number of students in SWE: ${result[2].length}. List: ${result[2].toString().split(',').join(', ')}`);
  } catch (err) { if (err.code === 'ENOENT') { throw new Error('Cannot load the database'); } }
}

module.exports = countStudents;
