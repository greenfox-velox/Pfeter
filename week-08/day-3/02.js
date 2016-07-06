'use strict';

// create a function takes three parameters:
//  - fileName: the name of the file
//  - letter: a character
//  - cb: callback (with two parameters: error and the result)
//
// it should read the file and count the letters in the content
// and it should call the callback with the counted number
// if there is some error it should call the callback with the error
//

const fs = require('fs');

function countLetters(fileName, letter, cb) {
  fs.readFile(fileName, function (err, fileContent) {
    if (err) {
      return cb(err);
    }
    const splittedContent = String(fileContent).split('', fileContent.length);
    const counted = splittedContent.filter(function (e) {
      return e === letter;
    }).length;
    cb(null, counted);
  });
}

countLetters('apple.txt', 'a', function (err, count) {
  console.log(count);
});
