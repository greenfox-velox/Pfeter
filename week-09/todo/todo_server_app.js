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

app.get('/todos', function (req, res) {
  con.query('SELECT * FROM todos WHERE destroyed = "false";', function (err, data) {
    if (err) {
      return console.log(err.toString());
    }
    res.json(data);
  });
});

app.get('/todos/:id', function (req, res) {
  con.query('SELECT * FROM todos WHERE todos.id = ?', req.params.id, function (err, data) {
    if (err) {
      return console.log(err.toString());
    }
    res.json(data[0]);
  });
});

app.put('/todos/:id', function (req, res) {
  const compStatus = (req.body.completed === 'false' && 'true') || (req.body.completed === 'true' && 'false');
  let newQuery = 'UPDATE todos SET completed = ? WHERE id = ?';
  const table = [compStatus, req.params.id];
  newQuery = mysql.format(newQuery, table);
  con.query(newQuery, function (err, data) {
    if (err) {
      return console.log(err.toString());
    }
    res.json(data);
  });
});

app.post('/todos', function (req, res) {
  con.query('INSERT INTO todos (text, completed) VALUES (?, "false");', req.body.text, function (err) {
    if (err) {
      return console.log(err.toString());
    }
    res.json([{
      id: res.insertId,
      text: req.body.text,
      completed: 'false',
    }]);
  });
});

app.delete('/todos/:id', function (req, res) {
  con.query('UPDATE todos SET destroyed = "true" WHERE id = ?', req.params.id, function (err) {
    if (err) {
      return console.log(err.toString());
    }
    res.json([{
      id: req.params.id,
      text: req.body.text,
      completed: req.body.completed,
      destroyed: 'true',
    }]);
  });
});

app.listen(3000);
console.log('Server running');
