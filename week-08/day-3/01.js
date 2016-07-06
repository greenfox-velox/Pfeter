'use strict';

const fs = require('fs');

const filterEmpty = function (e) {
  return e.length > 0;
};

function countWords(fileName, callback) {
  fs.readFile(fileName, function (err, content) {
    if (err) {
      return callback(err);
    }
    const counted = String(content).split(/\s/g).filter(filterEmpty).length;
    callback(null, counted);
  });
}

countWords('apple.txt', function (err, count) {
  console.log(count);
});
