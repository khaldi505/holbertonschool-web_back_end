const Fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    Fs.readFile(path, (err, databaseFile) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      const databasefile = databaseFile.toString().split('\n');
      databasefile.shift();
      const numOfStudents = databasefile.length;
      const result = [`Number of students: ${numOfStudents}`, [], []];
      databasefile.forEach((element) => {
        const resultElement = element.split(',');
        if (resultElement[3] === 'CS') {
          result[1].push(resultElement[0]);
        } else if (resultElement[3] === 'SWE') { result[2].push(resultElement[0]); }
      });
      const finalResult = `${result[0]}\nNumber of students in CS: ${result[1].length}. List: ${result[1].toString().split(',').join(', ')}\nNumber of students in SWE: ${result[2].length}. List: ${result[2].toString().split(',').join(', ')}`;
      console.log(finalResult);
      resolve(finalResult);
    });
  });
}

module.exports = countStudents;
