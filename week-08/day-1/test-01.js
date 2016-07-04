'use strict';

const e01 = require('./e01');
const tape = require('tape');

tape(function (t) {
  t.deepEqual(e01.countLetters('apple'), { a: 1, p: 2, l: 1, e: 1 });
  t.end();
});
