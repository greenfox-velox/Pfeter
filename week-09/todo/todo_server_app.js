'use strict';
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(express.static('public'));

const mysql = require('mysql');

const con = mysql.createConnection({
  host: '*',
  user: '*',
  password: '*',
  database: '*',
});

con.connect(function (err) {
  if (err) {
    console.log('Error connecting to Db');
    return;
  }
  console.log('Connection established');
});

app.get('/todos', function (req, res) {
  con.query('SELECT * FROM todos;',function(err, data){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.json(data);
  });
});

// con.query('INSERT INTO todos (text, completed) VALUES (?, 'false');' req.body.text, funtion....

// app.post('/todos', function (req, res) {
//   const newTodo = {
//     completed: false,
//     id: data.length + 1, // helyette a szervertől kellene lekérdezni az id-t
//     text: req.body.text,
//   };
//   data.push(newTodo);
//   res.json(newTodo);
// });

app.get('/todos/:id', function (req, res) {
  con.query('SELECT * FROM todos WHERE todos.id = ?', req.params.id, function (err, data){
    if(err) {
      console.log(err.toString());
      return;
    }
    res.json(data[0]);
  });
});

app.put('/todos/:id', function (req, res) {
  con.query('UPDATE todos SET completed = "true" WHERE id = ?', req.params.id, function (err, data){
    if(err) {
      console.log(err.toString());
      return;
    }
    con.
    res.json(data[0]);
  });
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

app.use(function (err, req, res, next) {
  res.sendStatus(404);
  next();
});

app.listen(3000);
console.log('Server running');
