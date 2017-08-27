import logging
import traceback

from flask_restplus import Api

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Grozeille Home API',
          description='Do what you wanna do :)')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

