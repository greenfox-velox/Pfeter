'use strict';

var y = 'seasons';
var out = 6;
// if the last and the first letter of the string
// are the same double the variable
// called out, if not half it
if (y[0] == y[y.length-1]) {
    out *= 2;
} else {
    out /= 2;
}
console.log(out);
