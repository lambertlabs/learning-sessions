import os
import subprocess


class SetUserAgentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        os.environ['USER_AGENT'] = request.META['HTTP_USER_AGENT']
        response = self.get_response(request)
        return response


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        subprocess.run('echo "$(date): Request to %s" >> request.log' % request.path, shell=True)
        response = self.get_response(request)
        return response
