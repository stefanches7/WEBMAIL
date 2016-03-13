sudo ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart


sudo ln -sf /home/box/web/conf/hello.py /etc/gunicorn.d/hello.py
sudo ln -sf /home/box/web/hello.py /usr/local/lib/python2.7/hello.py
sudo /etc/init.d/gunicorn restart
sudo gunicorn -b 0.0.0.0:8080 hello:app --access-logfile logs/guni.access.log --log-file logs/guni.log &
