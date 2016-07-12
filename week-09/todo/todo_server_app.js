'use strict';
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

const data = [
  {
    id: 1,
    text: 'Buy milk',
    completed: false,
  },
  {
    id: 2,
    text: 'Make dinner',
    completed: false,
  },
  {
    id: 3,
    text: 'Save the world',
    completed: false,
  },
];

app.get('/todos', function (req, res) {
  res.json(data);
});

app.post('/todos', function (req, res) {
  const newTodo = {
    completed: false,
    id: data.length + 1,
    text: req.body.text,
  };
  data.push(newTodo);
  res.json(newTodo);
});

app.get('/todos/:id', function (req, res) {
  res.json(data.filter(function (e) {
    if (e.id === +req.params.id) {
      return e;
    }
  })[0]);
});

app.put('/todos/:id', function (req, res) {
  res.json(data.filter(function (e) {
    if (e.id === +req.params.id) {
      e.text = req.body.text;
      e.completed = true;
      return e;
    }
  })[0]);
});

app.delete('/todos/:id', function (req, res) {
  res.json(data.filter(function (e) {
    if (e.id === +req.params.id) {
      e.destroyed = true;
      data.splice(data.indexOf(e), 1);
      return e;
    }
  })[0]);
});

app.listen(3000);
console.log('Server running');
