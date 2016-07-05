'use strict';


// create a function that takes a string and a letter and returns a boolean
// it should return true if the string consits the given letter, false otherwise

function isConsits(inputString, letter) {
  return inputString.split('', inputString.length).some(function (e) {
    return e === letter;
  });
}

console.log(isConsits('asdfg', 'g'));
