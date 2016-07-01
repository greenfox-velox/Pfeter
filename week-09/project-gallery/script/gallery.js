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
const thumbnails = document.querySelectorAll('.thumbnailpic');
const thumbHalf = Math.floor(thumbnails.length / 2);
const leftArrow = document.querySelector('.arrow.left');
const rightArrow = document.querySelector('.arrow.right');

let bigPicIndex = 0;
document.querySelector('.bigpicture').src = picsUrls[bigPicIndex];

function thumbnailChange() {
  for (let thumbIndex = 0; thumbIndex < thumbnails.length; thumbIndex++) {
    if (bigPicIndex - thumbHalf + thumbIndex < 0) {
      thumbnails[thumbIndex].src = picsUrls[picsUrls.length - thumbHalf + thumbIndex + bigPicIndex];
    } else if (bigPicIndex + thumbIndex > picsUrls.length - 1 + thumbHalf) {
      thumbnails[thumbIndex].src = picsUrls[Math.abs(picsUrls.length - bigPicIndex - thumbIndex + thumbHalf)];
    } else {
      thumbnails[thumbIndex].src = picsUrls[bigPicIndex - thumbHalf + thumbIndex];
    }
  }
}

thumbnailChange();

function changePicture(direction) {
  return function () {
    if (direction === 'next') {
      if (bigPicIndex >= picsUrls.length - 1) {
        bigPicIndex = 0;
      } else {
        bigPicIndex++;
      }
    } else if (direction === 'previous') {
      if (bigPicIndex <= 0) {
        bigPicIndex = picsUrls.length - 1;
      } else {
        bigPicIndex--;
      }
    }
    document.querySelector('.bigpicture').src = picsUrls[bigPicIndex];
    thumbnailChange();
  }; }

rightArrow.addEventListener('click', changePicture('next'));
leftArrow.addEventListener('click', changePicture('previous'));
