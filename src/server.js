var fs = require('fs'),
    http = require('http'),
    https = require('https'),
    express = require('express');

var port = 8000;

var options = {
    key: fs.readFileSync('src/SSL/key.pem'),
    cert: fs.readFileSync('src/SSL/cert.pem'),
};

var app = express();

app.use(express.static('src'))
app.use('/css', express.static(__dirname + 'src/css'))
app.use('/js', express.static(__dirname + 'src/js'))

app.get('', (req, res) => {
  res.sendFile(__dirname + '/html/index.html')
})

var server = https.createServer(options, app).listen(port, function(){
  console.log("Express server listening on port " + port);
});

