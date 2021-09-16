def my_web_app(environ, start_response):
    start_response('200', [])
    return [b'hi there']
