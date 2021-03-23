import uuid
import random
import string

class Session():


    @staticmethod
    def gen_session_uid(size):

        _chars = string.ascii_letters + string.digits + "@=-#"
        _uid = ''.join([random.choice(_chars) for i in range(size)])

        return _uid


    @staticmethod
    def get_registry():

        return SessionRegistry


    def __init__(self, remote, username):

        self._remote = remote.strip()
        self._username = username
        self._session_token = str(uuid.uuid4())
        self._session_key = Session.gen_session_uid(64)


    def get_remote(self):

        return self._remote

    
    def set_remote(self, remote):

        return self._remote


    def get_username(self):

        return self._username

    
    def set_username(self, username):

        return self._username


class SessionRegistry():

    SESSIONS = {}

    @staticmethod
    def add(session):

        SessionRegistry.SESSIONS[session.get_remote()] = session


    @staticmethod
    def remove(session):

        try:

            del SessionRegistry.SESSIONS[session.get_remote()]
            return True

        except:

            return False


    @staticmethod
    def clear_registry():

        SessionRegistry.SESSIONS = {}


    @staticmethod
    def get_sessions():

        return SessionRegistry.SESSIONS


    @staticmethod
    def find_session_by_remote(remote):

        return SessionRegistry.SESSIONS.get(remote.strip())


    @staticmethod
    def find_session_by_username(username):
        
        return True