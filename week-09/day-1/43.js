'use strict';

const numbers = [3, 4, 5, 6, 7];
// write a function that filters the odd numbers
// from an array and returns a new array consisting
// only the evens

function filterOddNumbers(input) {
  const output = [];
  for (let i = 0; i < input.length; i++) {
    if (input[i] % 2 === 0) {
      output.push(input[i]);
    }
  }
  return output;
}

console.log(filterOddNumbers(numbers));
