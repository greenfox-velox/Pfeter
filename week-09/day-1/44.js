'use strict';

const numbers = [7, 5, 8, -1, 2];
// Write a function that returns the minimal element
// in an array (your own min function)

function minElement(input) {
  let output = input[0];
  for (let i = 1; i < input.length; i++) {
    if (input[i] < output) {
      output = input[i];
    }
  }
  return output;
}

console.log(minElement(numbers));
