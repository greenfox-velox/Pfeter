'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 2, p: 2, l: 1}

function countStringLetters(string) {
  const output = {};
  string.split('', string.length).forEach(function (e) {
    output[e] = string.split('', string.length).filter(function (a) {
      return a === e;
    }).length;
  });
  return output;
}

console.log(countStringLetters('apple'));
