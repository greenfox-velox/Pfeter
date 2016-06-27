'use strict';

// create a function that returns it's input factorial

function factorial(input) {
  let summa = 1;
  for (let i = 1; i <= input; i++) {
    summa *= i;
  }
  return summa;
}

console.log(factorial(12));
