const express = require('express');
const app = express();
const fs = require('fs');
const port = parseInt(fs.readFileSync('port.txt'));
const mysql = require('mysql');

var con = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    database: 'thads',
    password: 'nut',
    multipleStatements: true,
});

app.get('/sql', (req, res) => {
    con.query(req.query.sql, function (err, results, fields) {
        if (err) {
            res.send({'error': err});
            console.log(err);
            return;
        }
        if (!parseInt(req.query.multiple)) {
            results = [results];
            fields = [fields];
        }
        // map the data so that we just have one for each column
        var response = [];
        results.forEach(function (result, idx) {
            to_send = {}
            fields[idx].forEach(function (field) {
                to_send[field.name] = [];
                result.forEach(function (row) {
                    to_send[field.name].push(row[field.name]);
                });
            })
            response.push(to_send);
        });
        res.send(JSON.stringify({result: response}));
    })
});

app.use('/', express.static('files'));

app.listen(port, () => console.log('we goin! on ' + port));
