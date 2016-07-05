'use strict';

var ab = 123;
var credits = 100;
var is_bonus = false;
// if credits are at least 50,
// and is_bonus is false, decrement ab by 2
// if credits are smaller than 50,
// and is_bonus is false, decrement ab by 1
// if is_bonus is true, ab should remain the same
if (!is_bonus) {
    if (credits >= 50) {
        ab -= 2
    } else {
        ab -= 1
    }
}

console.log(ab)
