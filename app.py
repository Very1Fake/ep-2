from os import path, environ
import bottle

import routes


if __name__ == '__main__':
    PROJECT_ROOT = path.abspath(path.dirname(__file__))
    STATIC_ROOT = path.join(PROJECT_ROOT, 'static').replace('\\', '/')
    HOST = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 8080

    @bottle.route('/static/<filepath:path>')
    def server_static(filepath):
        return bottle.static_file(filepath, root=STATIC_ROOT)

    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)
