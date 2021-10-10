from flask import Flask
from flaskr.api import bp as bp_api


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False,
        RESTPLUS_MASK_SWAGGER = False )


    # adicionar rotas
    app.register_blueprint(bp_api)
    return app