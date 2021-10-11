const Fs = require('fs');

function countStudents(path) {
  try {
    let databaseFile = Fs.readFileSync(path, 'utf8').toString();
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
    const finalResult = `${result[0]}\nNumber of students in CS: ${result[1].length}. List: ${result[1].toString().split(',').join(', ')}\nNumber of students in SWE: ${result[2].length}. List: ${result[2].toString().split(',').join(', ')}`;
    console.log(finalResult);
  } catch (err) {
    if (err.code === 'ENOENT') {
      throw new Error('Cannot load the database');
    }
  }
}

module.exports = countStudents;
