def myapp(environ, start_response):
  lst = environ["QUERY_STRING"].split('&')
  response = ''
  for query_item in lst:
    s+=query_item+"\n"
  start_reponse("200 OK", [("Content-Type", "text/plain"),("Content-Length",str(len(lst)))])
  return response
  
