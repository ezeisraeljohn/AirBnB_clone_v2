#!/usr/bin/env bash
#Configuring two web servers

# Install nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories if they don't exist
sudo mkdir -p /data/web_static/releases/test/ /data/web_static/shared/

# Create a fake HTML file for testing
echo "<html><head></head><body>Test Page</body></html>" | sudo tee /data/web_static/releases/test/index.html

# Create or recreate symbolic link
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

# Give ownership of /data/ folder to ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update nginx configuration
config_content="server {
    listen 80;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current/;
        index index.html;
    }
}"

echo "$config_content" | sudo tee /etc/nginx/sites-available/default

# Create a symbolic link to the new configuration
sudo ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
# Restart nginx
sudo service nginx restart
