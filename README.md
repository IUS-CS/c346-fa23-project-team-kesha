Instagram Comment Scraper<a name="TOP"></a>
===================
This project is meant to login to an existing Instagram/Facebook account and scrape comments from your recently liked videos. This project will also include a filter feature to search through comments for specific keywords.
- - - - - - - - -
# Basic Setup #

If you don't have Node.js downloaded, do so [here](https://nodejs.org/en/download)

Now, to install express(if you haven't done so already), run the following command:

    $ npm install express --save
  
- - - - - - - - - 

# Server Setup #

Features will be tested on your local server, so to run the webserver, run the following command from the main folder:

    $ node src/.vscode/server.js

This will host a website on your localhost with your SSL key and run the scripts in /src/js. Changes made to the web application visually will be made in the html and css folders.

- - - - - - - - - 

# Generate SSL Certificate and Key #

If you don't have your own SSL certificate and keys, you can generate them by running the following command: 

    $ openssl req -newkey rsa:2048 -new -nodes -x509 -days 3650 -keyout key.pem -out cert.pem

You will be prompted with a few questions. 

Next, copy those file and write them to /src/SSL/cert.pem and /src/SSL/key.pem

- - - - - - - - - 


  
