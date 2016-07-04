'use strict';

const e02 = require('./e02');
const tape = require('tape');

tape(function (t) {
  t.deepEqual(e02.countsBooks([
    { name: 'Steve', age: 12, books: ['Harry Potter', 'Lord of the Rings'] },
    { name: 'Ryan', age: 11, books: ['The funcdation'] },
    { name: 'Sheela', age: 14 },
    { name: 'Charlee', age: 9, books: [] },
    { name: 'Jessica', age: 12, books: ['Dune'] },
    { name: 'Robert', age: 15 },
  ]), 4);
  t.end();
});
