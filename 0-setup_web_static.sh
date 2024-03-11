#!/usr/bin/env bash
# setup webserver

sudo apt-get -y update
sudo apt-get -y install nginx

sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared

echo '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>' > /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data
sudo sed -i '/^server {/a\
    location /hbnb_static/ {\
        alias /data/web_static/current/;\
    }\
' /etc/nginx/sites-available/default

sudo service nginx restart
