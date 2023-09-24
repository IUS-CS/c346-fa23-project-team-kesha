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

var app = express();

app.use(express.static('src'));

// Meta (Facebook) App credentials
var clientId = 'ENTER CLEINT ID HERE';
var clientSecret = 'ENTER SECRET HERE';
var redirectUri = 'http://localhost:8000/auth/facebook/callback'; // need to replace once we get a url

// Endpoint to initiate OAuth
app.get('/auth/facebook', function (req, res) {
  var authUrl = 'https://www.facebook.com/v17.0/dialog/oauth?' +
    querystring.stringify({
      client_id: clientId,
      redirect_uri: redirectUri,
      scope: 'public_profile,email',
    });

  res.redirect(authUrl);
});

// Callback route after the user authorizes the app
app.get('/auth/facebook/callback', function (req, res) {
  var code = req.query.code;

  // Exchange the authorization code for an access token
  var tokenUrl = 'https://graph.facebook.com/v17.0/oauth/access_token?' +
    querystring.stringify({
      client_id: clientId,
      client_secret: clientSecret,
      redirect_uri: redirectUri,
      code: code,
    });

  https.get(tokenUrl, function (tokenResponse) {
    var body = '';

    tokenResponse.on('data', function (chunk) {
      body += chunk;
    });

    tokenResponse.on('end', function () {
      var tokenData = JSON.parse(body);

      // Use the access token to make API requests on behalf of the user
      var accessToken = tokenData.access_token;

      // API request to fetch user data
      https.get('https://graph.facebook.com/v17.0/me?fields=id,email', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }, function (apiResponse) {
        var apiData = '';

        apiResponse.on('data', function (apiChunk) {
          apiData += apiChunk;
        });

        apiResponse.on('end', function () {
          var userData = JSON.parse(apiData);

          // Handle user data here
          console.log('User data:', userData);

          // Redirect to a profile page or respond as needed
          res.redirect('/profile');
        });
      });
    });
  });
});

// Define a route for /profile
app.get('/profile', function (req, res) {
  res.send('This is the user profile page.');
});

var server = https.createServer(options, app).listen(port, function () {
  console.log("Express server listening on port " + port);
});