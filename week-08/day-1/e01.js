'use strict';

// create a function that takes a string and counts its letters
// it should return an object thats keys are the letters and the values are
// the counts.
// example: "apple" -> {a: 1, p: 2, l: 1, e: 1}

function countLetters(inputString) {
  return inputString.split('', inputString.length).reduce(function (acc, e) {
    acc[e] = (acc[e] + 1) || 1;
    return acc;
  }, { });
}

module.exports.countLetters = countLetters;
