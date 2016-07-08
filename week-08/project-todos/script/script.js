'use strict';

function showTodo(newElement) {
  const newLi = document.createElement('li');
  const newInput = document.createElement('input');
  const newLabel = document.createElement('label');
  const newImg = document.createElement('img');
  document.querySelector('.todo-items').appendChild(newLi);
  newLi.appendChild(newLabel);
  newLabel.textContent = newElement.text;
  newLabel.id = newElement.id;
  newLi.appendChild(newImg);
  newImg.id = newElement.id;
  newImg.src = 'image/trash.png';
  newImg.classList.add('trash');
  newLi.appendChild(newInput);
  newInput.type = 'checkbox';
  newInput.id = newElement.id;
  newInput.checked = newElement.completed;
}

function pageOnload() {
  const xhr = new XMLHttpRequest();
  xhr.onload = function () {
    JSON.parse(xhr.response).forEach(function (e) {
      showTodo(e);
    });
  };
  xhr.open('GET', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.send();
}

function addTodo() {
  const xhr = new XMLHttpRequest();
  const inputText = document.querySelector('input').value;
  const allLi = document.querySelectorAll('li label');
  const nextId = parseInt(allLi[allLi.length - 1].id) + 1;
  const inputValue = { id: nextId, text: inputText, completed: false };
  xhr.open('POST', 'https://mysterious-dusk-8248.herokuapp.com/todos');
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(inputValue));
  showTodo(inputValue);
}

document.querySelector('.add-button').addEventListener('click', function () {
  addTodo();
});

document.querySelector('ul').addEventListener('click', function () {
  console.log(event.target.id);
});

pageOnload();
