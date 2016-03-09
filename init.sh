sudo apt-get update
sudo apt-get install nginx
sudo ln -sf /home/box/web/etc/nginx.conf  etc/nginx/sites-enabled/test.conf
sudo etc/init.d/nginx restart
