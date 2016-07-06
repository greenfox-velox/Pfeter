'use strict';

// Create a function that takes 3 parameters
//  - file1: a filename
//  - file2: a filename
//  - cb: callback (with two paramteres: error and contents)
//
// It should read both files and concat their content
// then it should call the callback with the concated contents
// if any error occures it should call the callback with an error

const fs = require('fs');

function doubleContent(file1, file2, cb) {
  fs.readFile(file1, function (err, file1Content) {
    if (err) {
      return cb(err);
    }
    const content1 = String(file1Content).trim();
    fs.readFile(file2, function (err2, file2Content) {
      if (err2) {
        return cb(err2);
      }
      const content2 = String(file2Content).trim();
      const concatenatedStrings = content1 + content2;
      cb(err2, concatenatedStrings);
    });
  });
}

doubleContent('apple.txt', 'orange.txt', function (err, concatenated) {
  console.log(concatenated);
});
