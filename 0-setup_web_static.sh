#!/usr/bin/env bash
#does what you see

sudo apt update
sudo apt install -y nginx
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared
sudo chown -R ubuntu:ubuntu /data/

echo "my test deployment" >> /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

sudo tee  /etc/nginx/sites-available/default > /dev/null <<EOT
server {
    listen 	80 default_server;
    listen 	[::]:80 default_server;
    add_header 	X-Served-By $HOSTNAME;
    root   	/var/www/html;
    index  	index.html index.htm;

    location /hbnb_static {
        alias 	/data/web_static/current/;
        index 	index.html index.htm;
    }

    location /redirect_me {
        return 	301 http://cuberule.com/;
    }

    error_page 404 /404.html;
    location /404 {
      root 	/var/www/html;
      internal;
    }
}
EOT

sudo service nginx restart
