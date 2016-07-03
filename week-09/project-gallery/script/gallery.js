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

function thumbnailChange() {
  for (let thumbIndex = 0; thumbIndex < thumbnails.length; thumbIndex++) {
    const thumbPictureIndex = thumbIndex + bigPicIndex - thumbHalf;
    if (thumbPictureIndex < 0) {
      thumbnails[thumbIndex].src = picsUrls[picsUrls.length + thumbPictureIndex];
    } else if (bigPicIndex + thumbIndex > picsUrls.length - 1 + thumbHalf) {
      thumbnails[thumbIndex].src = picsUrls[Math.abs(picsUrls.length - thumbPictureIndex)];
    } else {
      thumbnails[thumbIndex].src = picsUrls[thumbPictureIndex];
    }
  }
}

function drawer() {
  document.querySelector('.bigpicture').src = picsUrls[bigPicIndex];
  thumbnailChange();
}

function nextPicture() {
  if (bigPicIndex >= picsUrls.length - 1) {
    bigPicIndex = 0;
  } else {
    bigPicIndex++;
  }
  drawer();
}

function previousPicture() {
  if (bigPicIndex <= 0) {
    bigPicIndex = picsUrls.length - 1;
  } else {
    bigPicIndex--;
  }
  drawer();
}

drawer();
rightArrow.addEventListener('click', nextPicture);
leftArrow.addEventListener('click', previousPicture);
