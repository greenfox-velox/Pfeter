'use strict';

const xhr = new XMLHttpRequest();

function todosToList(newElement) {
  console.log(newElement);
  const newLabel = document.createElement('label');
  const newInput = document.createElement('input');
  const newImg = document.createElement('img');
  document.querySelector('.todo-item').appendChild(newLabel);
  newLabel.textContent = newElement.text;
  newLabel.id = newElement.id;
  newLabel.appendChild(newImg);
  newImg.id = newElement.id;
  newImg.src = 'image/trash.png';
  newImg.classList.add('trash');
  newLabel.appendChild(newInput);
  newInput.type = 'checkbox';
  newInput.value = newElement.id;
}

xhr.onload = function () {
  JSON.parse(xhr.response).forEach(function (e) {
    todosToList(e);
  });
};

xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
xhr.send();
