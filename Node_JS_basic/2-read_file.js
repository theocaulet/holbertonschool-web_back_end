const fs = require('fs');

function countStudents(path) {
  try {
    const database = fs.readFileSync(path, 'utf8').split('\n').filter((line) => line.trim() !== '').slice(1);
    const groups = {};
    database.forEach((line) => {
      const parts = line.split(',');
      const firstname = parts[0];
      const field = parts[3];
      if (groups[field]) {
        groups[field].push(firstname);
      } else {
        groups[field] = [firstname];
      }
    });
    console.log(`Number of students: ${database.length}`);
    for (const field in groups) {
      if (Object.prototype.hasOwnProperty.call(groups, field)) {
        console.log(`Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`);
      }
    }
  } catch (error) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
