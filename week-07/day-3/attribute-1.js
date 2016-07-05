// Write the image's url to the console.
var imageUrl = document.querySelector('img').src;
console.log(imageUrl);
// Replace the image with a picture of yourself.
document.querySelector('img').src = '1.png';
// Make the link point to the Green Fox Academy website.
document.querySelector('a').href = 'http://www.greenfoxacademy.com/';
// Disable the second button.
document.querySelector('.this-one').disabled = true;
// Replace its text with 'Don't click me!'.
document.querySelector('.this-one').textContent = "Don't click me!";
