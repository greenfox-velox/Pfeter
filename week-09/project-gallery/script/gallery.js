'use strict';

const picsUrls = [
  'images/1.jpg',
  'images/2.jpg',
  'images/3.jpg',
  'images/4.jpg',
  'images/5.jpg',
  'images/6.jpg',
  'images/7.jpg',
  'images/8.jpg',
  'images/9.jpg',
  'images/10.jpg',
];
const leftArrow = document.querySelector('.arrow.left');
const rightArrow = document.querySelector('.arrow.right');

let bigPictureIndex = 0;
document.querySelector('.bigpicture').src = picsUrls[bigPictureIndex];

function nextPicture() {
  if (bigPictureIndex < picsUrls.length - 1) {
    bigPictureIndex++;
    document.querySelector('.bigpicture').src = picsUrls[bigPictureIndex];
  }
}

function previousPicture() {
  if (bigPictureIndex > 0) {
    bigPictureIndex--;
    document.querySelector('.bigpicture').src = picsUrls[bigPictureIndex];
  }
}

rightArrow.addEventListener('click', nextPicture);

leftArrow.addEventListener('click', previousPicture);
