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
    return console.log('Error connecting to Db');
  }
  console.log('Connection established');
});

// con.end();

app.get('/todos', function (req, res) {
  con.query('SELECT * FROM todos;',function(err, data){
    if(err) {
      return console.log(err.toString());
    }
    res.json(data);
  });
});

app.get('/todos/:id', function (req, res) {
  con.query('SELECT * FROM todos WHERE todos.id = ?', req.params.id, function (err, data){
    if(err) {
      return console.log(err.toString());
    }
    res.json(data[0]);
  });
});

app.put('/todos/:id', function (req, res) {
  con.query('UPDATE todos SET completed = "true" WHERE id = ?', req.params.id, function (err, data){
    if(err) {
      return console.log(err.toString());
    }
    con.
    res.json(data[0]);
  });
});

app.post('/todos', function (req, res) {
  con.query('INSERT INTO todos (text, completed) VALUES (?, "false");', req.body.text, function (err, data) {
    if(err) {
      return console.log(err.toString());
    }
    con.query('SELECT * FROM todos WHERE id = ? AND text = ?', res.insertId, req.body.text, function (err, newData) {
      if(err) {
        return console.log(err.toString());
      }
      res.json(newData[0]);
    });
  });
});

app.delete('/todos/:id', function (req, res) {
  con.query('UPDATE todos SET destroyed = "true" WHERE id = ?', req.params.id, function (err, data) {
    if(err) {
      return console.log(err.toString());
    }
    con.query('SELECT * FROM todos WHERE id = ?', req.params.id, function (err, result) {
      if (err) {
        return console.log(err.toString());
      }
      res.json(result[0]);
    });
  });
});

app.use(function (err, req, res, next) {
  res.sendStatus(404);
  next();
});

app.listen(3000);
console.log('Server running');
