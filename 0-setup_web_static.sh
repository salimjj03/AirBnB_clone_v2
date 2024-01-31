#!/usr/bin/env bash
#sets up your web servers for the deployment of web_static
if ! command -v nginx &> /dev/null; then
	apt-get -y update
	apt-get -y install nginx
fi
mkdir -p /data/web_static/releases/test
mkdir -p /data/web_static/shared/
echo "Hello World!" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
tx="location /hbnb_static"
if  ! grep -q "$tx" /etc/nginx/sites-available/default; then
	sed -i  "/server_name _/a\\
	\\
	$tx {\\
		alias /data/web_static/current;\\
	}" /etc/nginx/sites-available/default
fi
service nginx restart
