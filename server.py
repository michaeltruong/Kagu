from gevent import pywsgi


def hello_world(environ, start_response):
    f = open('tweet.txt', 'r')
    tweet = f.read()
    
    start_response('200 OK', [('Content-Type', 'text/html')])
    while True:
        yield tweet

server = pywsgi.WSGIServer(
    ('', 8080), hello_world)

server.serve_forever()
