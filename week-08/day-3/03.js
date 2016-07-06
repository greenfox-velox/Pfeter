'use strict';

// create a function that takes 3 parameters
//  - readFileName: a filename where it reads from
//  - wirteFileName: a filename where it writes to
//  - cb: callback with one parameter: the error if occured
//
// It should read the file named readFileName and double the text of the file
// like: "apple" -> "appleapple"
// Than it should write this doubled text to the file named writeFileName
// When it finished it should call the callback with a null
// If there is any error during the process it should call the callback with the error

const fs = require('fs');

function doubleContent(readFileName, wirteFileName, cb) {
  fs.readFile(readFileName, function (err, fileContent) {
    if (err) {
      return cb(err);
    }
    const doubledContent = String(fileContent).trim();
    fs.writeFile(wirteFileName, doubledContent + doubledContent, function (err2) {
      if (err2) {
        return cb(err2);
      }
      cb(null);
    });
  });
}

doubleContent('apple2.txt', 'doubleapple.txt', function (err) {
  if (err) {
    console.log(err);
  }
});
