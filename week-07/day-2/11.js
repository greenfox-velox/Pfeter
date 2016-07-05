'use strict';

// Create a `Stack` constructor that stores elements
// It should have a `size` method that returns number of elements it has
// It should have a `push` method that adds an element to the stack
// It should have a `pop` method that returns the last
// element form the stack and also deletes it from it

// please don`t use the built in methods

function Stack(elements) {
  this.elements = elements;
  this.size = function () {
    let stackSize = 0;
    this.elements.forEach(function () {
      stackSize++;
    });
    return stackSize;
  };
  this.push = function (pushElement) {
    this.elements[this.size()] = pushElement;
  };
  this.pop = function () {
    this.elements.length--;
    // this.elements.pop();
  };
}

const stack = new Stack(['1', '2', '3', '4', 'b', 'c']);

console.log(stack.size());
stack.push('a');
console.log(stack.size());
stack.pop();
console.log(stack.size());
