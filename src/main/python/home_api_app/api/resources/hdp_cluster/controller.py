import logging

from flask import request
from flask_restplus import Resource
from home_api_app.api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('hdp_cluster', description='Operations related to the hdp cluster')


@ns.route('/')
class Cluster(Resource):

    def get(self):
        """
        Returns the status of the cluster
        """
        return True

    @api.response(201, 'Cluster successfully created.')
    @api.expect()
    def post(self):
        """
        Deploy the cluster
        """
        return None, 201

    @api.response(204, 'Cluster successfully deleted.')
    def delete(self, id):
        """
        Deletes the cluster.
        """
        return None, 204