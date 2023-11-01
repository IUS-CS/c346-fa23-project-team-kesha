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

module.exports = app;

app.use(express.static('src'));

// Meta (Facebook) App credentials
var clientId = '1013165189995871'; // need to replace once we get a client id
var clientSecret = 'f5c3498ab5cf5d90ec7263b3dc8a469c';
var redirectUri = 'https://localhost:8000/auth/facebook/callback'; // need to replace once we get a url

//test page
app.get('/test', function (req, res) {
  res.code(200);
  res.send('This is a test page.');
});

// Endpoint to initiate OAuth
app.get('/auth/facebook', function (req, res) {
  var authUrl = 'https://www.facebook.com/v18.0/dialog/oauth?' +
    querystring.stringify({
      client_id: clientId,
      redirect_uri: redirectUri,
      scope: 'public_profile,email,user_likes',
    });

  res.redirect(authUrl);
});

var userData = '';

// Callback route after the user authorizes the app
app.get('/auth/facebook/callback', function (req, res) {
  var code = req.query.code;
  console.log('Received authorization code:', code);

  // Exchange the authorization code for an access token
  var tokenUrl = 'https://graph.facebook.com/v18.0/oauth/access_token?' +
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
      console.log('Token data:', tokenData);

      // Use the access token to make API requests on behalf of the user
      accessToken = tokenData.access_token;

      // API request to fetch user data
      https.get('https://graph.facebook.com/v18.0/me?fields=id,email,birthday', {
        headers: {
          Authorization: `Bearer ${accessToken}`,
        },
      }, function (apiResponse) {
        var apiData = '';

        apiResponse.on('data', function (apiChunk) {
          apiData += apiChunk;
        });

        apiResponse.on('end', function () {
          userData = JSON.parse(apiData);

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

  // Make a request to the Graph API to fetch the user's posts
  https.get(`https://graph.facebook.com/v18.0/me/posts?access_token=${accessToken}`, function (apiResponse) {
    var apiData = '';

    apiResponse.on('data', function (apiChunk) {
      apiData += apiChunk;
    });

    apiResponse.on('end', function () {
      const userPosts = JSON.parse(apiData);

      // Handle user posts here
      console.log('User posts:', userPosts);

      // Send the user posts as a JSON response
      res.json(userPosts);
    });
  });
});

// Define a route to automatically redirect from /profile to /profile-page
app.get('/profile', function (req, res) {
  res.redirect('/profile-page');
});

app.use(express.static('public')); // Serve static files from the "public" directory

app.get('/profile-page', function (req, res) {
  res.sendFile(__dirname + '/../html/profile.html');
});


var server = https.createServer(options, app).listen(port, function () {
  console.log("Express server listening on port " + port);
});