var fs = require('fs'),
    http = require('http'),
    https = require('https'),
    express = require('express');

var port = 8000;

var options = {
    key: fs.readFileSync('TikTok/SSL/key.pem'),
    cert: fs.readFileSync('TikTok/SSL/cert.pem'),
};

var app = express();

app.use(express.static('TikTok'));

var server = https.createServer(options, app).listen(port, function(){
  console.log("Express server listening on port " + port);
});

