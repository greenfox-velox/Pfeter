'use strict';

const names = ['Zakarias', 'Hans', 'Otto', 'Ole'];
// create a function that returns the shortest string
// from an array

function shortestString(input) {
  let output = input[0];
  for (let i = 1; i < input.length; i++) {
    if (input[i].length < output.length) {
      output = input[i];
    }
  }
  return output;
}

console.log(shortestString(names));
