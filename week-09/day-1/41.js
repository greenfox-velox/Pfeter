'use strict';

const numbers = [4, 5, 6, 7, 8, 9, 10];
// write your own sum function

function summ(input) {
  let summa = 0;
  for (let i = 0; i < input.length; i++) {
    summa += input[i];
  }
  return summa;
}

console.log(summ(numbers));
