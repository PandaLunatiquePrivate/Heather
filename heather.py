import os
import sys
import flask
import pathlib
import logging
import argparse
import ipaddress

from flask_cors import CORS as CORSHandle

from org.heather.setup import Setup
from org.heather.config import Config
from org.heather.profile import Profile
from org.heather.directory import Directory
from org.heather.database import Database
from org.heather.api.log import Log, LogLevel
from org.heather.api.tools import Tools
from org.heather.api.enums import StatusCode, StatusLiteral, StatusDetails
from org.heather.session import Session, SessionRegistry
from org.heather.request import Response
from org.heather.api.latency import LatencyCalculator


# Argument Parser
parser = argparse.ArgumentParser()
parser.add_argument('-setup', help='Start the Heather setup wizard.', action="store_true")
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

    processHandler = Config.load_config(os.path.dirname(__file__))
    processHandler = Setup.verify('./')

    print(Config.CONFIG)


endpoint = flask.Flask(__name__, template_folder='web')
endpoint.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
endpoint.config['JSONIFY_MIMETYPE'] = 'application/json'
endpoint.config['TEMPLATES_AUTO_RELOAD'] = True
endpoint.config['APPLICATION_ROOT'] = '/'
CORSHandle(endpoint)

endpointLogger = logging.getLogger('werkzeug')
endpointLogger.setLevel(logging.ERROR)

Database.connect(os.path.normpath(Config.CONFIG['parsed_paths']['database'] + '\\database.db'))

Profile.update_profiles()
Directory.update_directories()


@endpoint.route('/')
def main():

    sessionProfile = SessionRegistry.find_session_by_remote(flask.request.remote_addr)
    ipAddress = ipaddress.ip_address(flask.request.remote_addr)

    if sessionProfile != None:

        print('not none')
        return f'Connected on session {sessionProfile.get_session_token()} binded to {sessionProfile.get_remote()}'

    else:
        #newSession = Session(flask.request.remote_addr, '10')
        #SessionRegistry.add(newSession)

        if not ipAddress.is_private:
            return flask.render_template('profiles.html')
        else:
            return flask.render_template('profiles.html')




@endpoint.route('/api/v1/heather/profile/list', methods=['GET'])
def api_profile_list():

    requestUid = Tools.get_uid(16)
    LatencyCalculator.begin(requestUid)
    
    responseBuilder = Response.builder(requestUid, "v1")

    Profile.update_profiles()
    profilesInstances = Profile.get_profiles()
    
    profiles = []

    for p in profilesInstances:
        profiles.append({
            "id": profilesInstances[p].get_profile_id(),
            "uid": profilesInstances[p].get_profile_uid(),
            "group_uid": profilesInstances[p].get_profile_group_uid(),
            "name": profilesInstances[p].get_profile_name()
        })
        
    LatencyCalculator.end(requestUid)   

    responseBuilder['meta']['status_code'] = StatusCode.OK
    responseBuilder['meta']['status_literal'] = StatusLiteral.OK
    responseBuilder['meta']['status_details'] = StatusDetails.OK
    responseBuilder['meta']['execution'] = LatencyCalculator.result(requestUid)
    responseBuilder['result']['profiles'] = profiles

    return flask.jsonify(responseBuilder)


@endpoint.route('/cdn/static/<path:static>')
def cdn_static(static):

    return flask.send_from_directory('web', static)


@endpoint.errorhandler(404)
def error_404(e):
    return 'No!'

endpoint.run(host='0.0.0.0', port=8080, debug=True)


#TODO: API: Image Pixel Color Average calculator