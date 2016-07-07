'use strict';

const xhr = new XMLHttpRequest();
const textToYoda = document.querySelector('#textToYoda');

function sendToYodanize() {
  const askYoda = 'https://yoda.p.mashape.com/yoda?sentence=' + encodeURIComponent(textToYoda.value);
  xhr.onload = function () {
    document.querySelector('p').textContent = xhr.response;
  };
  xhr.open('GET', askYoda);
  xhr.setRequestHeader('X-Mashape-Key', 's4ya2m2rwjmshJrfThmkQfeJz4Hhp1PUxPmjsnD0dSPuct97Gw');
  xhr.send();
}

document.querySelector('.button').addEventListener('click', sendToYodanize);
