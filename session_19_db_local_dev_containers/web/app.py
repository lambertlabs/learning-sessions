import falcon
from falcon_autocrud.middleware import Middleware
from sqlalchemy import create_engine
from wsgiref.simple_server import make_server

from resources import UserCollectionResource


app = falcon.API(middleware=[Middleware()])

engine = create_engine('postgresql://myadmin:mypw@localhost/demo5')
users = UserCollectionResource(engine)
app.add_route('/users', users)

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')

        httpd.serve_forever()
