def myapp(environ, start_response)
  lst = environ["QUERY_STRING"].split('&')
  start_reponse("200 OK", [("Content-Type", "text/plain"),("Content-Length",str(len(lst)))])
  return iter(lst)
  
