from werkzeug.contrib.fixers import ProxyFix

def app(environ, start_response):
  lst = environ["QUERY_STRING"].split('&')
  response = ''
  for query_item in lst:
    s+=query_item+"\n"
  start_reponse('200 OK', [('Content-Type', 'text/plain'),("Content-Length",len(response)*8)])
  return response
  
app.wsgi_app = ProxyFix(app.wsgi_app)
app.run()
