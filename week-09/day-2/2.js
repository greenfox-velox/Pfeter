'use strict';

// create a function called apply that takes a function and calls it with one argument
// that is the string 'apple'

function apply(fun, a) {
  fun(a);
}

apply(console.log, 'apple'); // should log apple
