sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart
sudo mv /home/box/web/hello_config.py /home/box/etc/
sudo ln -sf /home/box/etc/hello_config.py  /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
gunicorn /home/box/web/hello.py
