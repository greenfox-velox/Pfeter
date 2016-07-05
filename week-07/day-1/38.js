'use strict';

// Write a program that prints the numbers from 1 to 100.
// But for multiples of three print "Fizz" instead of the number
// and for the multiples of five print "Buzz".
// For numbers which are multiples of both three and five print "FizzBuzz".
for (let i = 1; i < 101; i++) {
  let output = '';
  if (i % 3 === 0) {
    output = 'Fizz';
  }
  if (i % 5 === 0) {
    output += 'Buzz';
  }
  if (output === '') {
    output = String(i);
  }
  console.log(output);
}
