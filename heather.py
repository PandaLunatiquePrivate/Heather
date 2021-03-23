import os
import sys
import flask
import pathlib
import logging
import argparse

from flask_cors import CORS

from org.heather.setup import Setup
from org.heather.api.log import Log, LogLevel


# Argument Prser
parser = argparse.ArgumentParser()
parser.add_argument('-setup', help='Start the JHeather setup wizard.', action="store_true")
parser.add_argument('-fullreset', help='To do', action="store_true")
parser.add_argument('-resetconfig', '-rc', help='To do', action="store_true")
parser.add_argument('-nocolor', help='To do', action="store_true")
parser.add_argument('-force', help='To do', action="store_true")
parser.add_argument('-restore', help='To do', action="store_true")
parser.add_argument('-debug', help='To do', action="store_true")
args = parser.parse_args()

Log.do(LogLevel.ALL, 'Heather Project (C) 2021 - dev-1.0.0')

# Startup process
is_setup = Setup.is_config_valid(os.path.dirname(__file__))


# Start main setup wizard
if not is_setup or args.setup:

    Setup.wizard(os.path.dirname(__file__))
    sys.exit(-1)

# Process to main integrity verification
else:

    print('dat')


endpoint = flask.Flask(__name__)
CORS(endpoint)
endpoint.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@endpoint.route('/')
def main():

    return 'r'



endpoint.run(host='0.0.0.0', port=8080)