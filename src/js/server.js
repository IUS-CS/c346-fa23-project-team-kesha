const path = require('path')

var fs = require('fs'),
    http = require('http'),
    https = require('https'),
    express = require('express'),
    querystring = require('querystring'),
    port = 8000

var options = {
   key: fs.readFileSync('src/SSL/key.pem'),
   cert: fs.readFileSync('src/SSL/cert.pem'),
};

// Static Files for Homepage
var app = express();
app.use(express.static('src'));
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../html/index.html'))
});

var server = https.createServer(options, app).listen(port, function () {
  console.log("Express server listening on port " + port);
});