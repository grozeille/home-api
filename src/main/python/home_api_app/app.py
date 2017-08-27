import logging.config

from flask import Flask, Blueprint
from home_api_app.api.resources.hdp_cluster.controller import ns as hdp_cluster_namespace

from home_api_app.api.restplus import api

class App:
    def __init__(self, settings):
        self.log = logging.getLogger(__name__)
        self.settings = settings

    def start(self):
        self.app = Flask(__name__)

        self.configure_app()

        blueprint = Blueprint('api', __name__, url_prefix='/api')
        api.init_app(blueprint)
        api.add_namespace(hdp_cluster_namespace)
        self.app.register_blueprint(blueprint)

        self.log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(self.app.config['SERVER_NAME']))
        server_name_split = str(self.app.config['SERVER_NAME']).split(":")
        self.app.run(host=server_name_split[0], port=int(server_name_split[1]), debug=self.settings["FLASK_DEBUG"])


    def configure_app(self):
        self.app.config['SERVER_NAME'] = self.settings["FLASK_SERVER_NAME"]
        self.app.config['SWAGGER_UI_DOC_EXPANSION'] = self.settings["RESTPLUS_SWAGGER_UI_DOC_EXPANSION"]
        self.app.config['RESTPLUS_VALIDATE'] = self.settings["RESTPLUS_VALIDATE"]
        self.app.config['RESTPLUS_MASK_SWAGGER'] = self.settings["RESTPLUS_MASK_SWAGGER"]
        self.app.config['ERROR_404_HELP'] = self.settings["RESTPLUS_ERROR_404_HELP"]
