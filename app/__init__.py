import logging

from flasgger import Swagger
from flask import Flask
from .routes import api

logging.basicConfig(filename='record.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')


def create_app():
    app = Flask(__name__)
    app.logger.setLevel(logging.ERROR)
    handler = logging.StreamHandler()  # Create a stream handler for the logger
    app.logger.addHandler(handler)
    app.register_blueprint(api, url_prefix='/v1/api')
    Swagger(app)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
