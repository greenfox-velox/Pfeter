// 1. store the element that says 'The King' in the 'king' variable.
// console.log it.
var king = document.querySelector('#b325');
console.log(king);
// 2. store the element that contains the text 'The Conceited Man'
// in the 'conceited' variable.
// show the result in an 'alert' window.
var conceited = document.querySelector('.asteroid.b326');
alert(conceited);
// 3. store 'The Businessman' and 'The Lamplighter'
// in the 'businessLamp' variable.
// console.log each of them.
var businessLamp = document.querySelectorAll('.asteroid.big');
for (let e = 0; e < businessLamp.length; e++) {
  console.log(businessLamp[e]);
}
// 4. store 'The King' and 'The Conceited Man'
// in the 'conceitedKing' variable.
// alert them one by one.
var conceitedKing = document.querySelectorAll('.container .asteroid');
for (let f = 0; f < conceitedKing.length; f++) {
  alert(conceitedKing[f]);
}
// 5. store 'The King', 'The Conceited Man' and 'The Lamplighter'
// in the 'noBusiness' variable.
// console.log each of them.
var noBusiness = document.querySelectorAll('div.asteroid');
for (let g = 0; g < noBusiness.length; g++) {
  console.log(noBusiness[g]);
}
// 6. store 'The Businessman' in the 'allBizniss' variable.
// show the result in an 'alert' window.
var allBizniss = document.querySelectorAll('p.asteroid');
for (let g = 0; g < allBizniss.length; g++) {
  alert(allBizniss[g]);
}
