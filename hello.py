
def app(environ, start_response):
  lst = str(environ["QUERY_STRING"]).split('&')
  response = ''
  for query_item in lst:
    response+=query_item+"\n"
  return ('200 OK', [('Content-Type', 'text/plain'),("Content-Length",len(response)*8)], [response])
  
