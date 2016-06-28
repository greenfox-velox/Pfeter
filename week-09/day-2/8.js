'use strict';

const students = [
  { name: 'Rezso', age: 9.5, candies: 2 },
  { name: 'Gerzson', age: 10, candies: 1 },
  { name: 'Aurel', age: 7, candies: 3 },
  { name: 'Zsombor', age: 12, candies: 5 },
  { name: 'Olaf', age: 12, candies: 7 },
  { name: 'Teodor', age: 3, candies: 2 },
];


// create a function that counts the students that
// has more than 4 candies

function countStudentHas4Candies(input) {
  return input.filter(function (e) {
    return e.candies > 4;
  }).length;
}

console.log(countStudentHas4Candies(students));
