const express = require('express');
const app = express();
const fs = require('fs');
const port = parseInt(fs.readFileSync('port.txt'));

app.use('/', express.static('files'));

app.listen(port, () => console.log('we goin! on ' + port));
