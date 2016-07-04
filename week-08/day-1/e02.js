'use strict';


const students = [
  { name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings'] },
  { name: 'Ryan', age: 11, books: ['The funcdation'] },
  { name: 'Sheela', age: 14 },
  { name: 'Charlee', age: 9, books: [] },
  { name: 'Jessica', age: 12, books: ['Dune'] },
  { name: 'Robert', age: 15 },
];

// create a function that counts all the books of an array of students
// not every student has a property called books

var countsBooks = function (input) {
  return input.reduce(function (acc, e) {
    acc += (e.books || []).length;
    return acc;
  }, 0);
};

module.exports.countsBooks = countsBooks;

console.log(countsBooks(students));
