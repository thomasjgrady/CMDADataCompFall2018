const express = require('express');
const app = express();
const fs = require('fs');
const port = parseInt(fs.readFileSync('port.txt'));
const mysql = require('mysql');

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    database: 'thads',
    password: 'nut'
});

app.get('/sql', (req, res) => {
    con.query(req.query.sql, function (err, results, fields) {
        if (err) console.err(err);
        // map the data so that we just have an for each column
        to_send = {}
        fields.forEach(function (field) {
            to_send[field.name] = [];
            results.forEach(function (row) {
                to_send[field.name].push(row[field.name]);
            });
        })
        res.send(JSON.stringify({result: to_send}));
    })
});

app.use('/', express.static('files'));

app.listen(port, () => console.log('we goin! on ' + port));
