from werkzeug.contrib.fixers import ProxyFix
from flask import Flask
app = Flask(__name__)
def myapp(environ, start_response):
  lst = environ["QUERY_STRING"].split('&')
  response = ''
  for query_item in lst:
    s+=query_item+"\n"
  start_reponse("200 OK", [("Content-Type", "text\plain"),("Content-Length",str(len(lst)))])
  return response
  
app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == '__main__':
    app.run()
