'use strict';

const url = 'http://localhost:3000/todos';

function showTodo(newElement) {
  const newLi = document.createElement('li');
  const newInput = document.createElement('input');
  const newLabel = document.createElement('label');
  const newSection = document.createElement('section');
  const newImg = document.createElement('img');
  document.querySelector('.todo-items').appendChild(newLi);
  newLi.id = 'lilmt' + newElement.id;
  newLi.classList.add('flex-row');
  newLi.classList.add('spcbetween');
  newLi.appendChild(newLabel);
  newLabel.textContent = newElement.text;
  newLabel.id = 'label' + newElement.id;
  newLi.appendChild(newSection);
  newSection.appendChild(newImg);
  newImg.id = 'image' + newElement.id;
  newImg.src = 'image/trash.png';
  newImg.classList.add('trash');
  newSection.appendChild(newInput);
  newInput.type = 'checkbox';
  newInput.id = 'check' + newElement.id;
  newInput.classList.add('checkbox');
  newInput.checked = newElement.completed;
}

function pageOnload() {
  const xhr = new XMLHttpRequest();
  xhr.onload = function () {
    JSON.parse(xhr.response).forEach(function (e) {
      showTodo(e);
    });
  };
  xhr.open('GET', url);
  xhr.send();
}

function addTodo() {
  const xhr = new XMLHttpRequest();
  const inputText = document.querySelector('input').value;
  const allLi = document.querySelectorAll('li label');
  const nextId = parseInt(allLi[allLi.length - 1].id) + 1;
  const inputValue = { id: nextId, text: inputText, completed: false };
  xhr.open('POST', url);
  xhr.setRequestHeader('content-type', 'application/json');
  xhr.send(JSON.stringify(inputValue));
  showTodo(inputValue);
}

function destroyTodo(removeElementId) {
  const xhr = new XMLHttpRequest();
  document.querySelector('.todo-items').removeChild(document.querySelector('#' + removeElementId))
}

document.querySelector('.add-button').addEventListener('click', function () {
  addTodo();
});

document.querySelector('ul').addEventListener('click', function () {
  destroyTodo(event.target.id.slice(5));
});

pageOnload();
