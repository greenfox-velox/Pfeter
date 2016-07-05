'use strict';

const numbers = [2, 5, 11, 29];

// create a function that takes an array of numbers and returns a boolean
// it should return true if all the elements are prime, false otherwise

function isElementPrime(number) {
  for (let i = 2; i < number / 2 + 1; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}

console.log(numbers.every(isElementPrime));
