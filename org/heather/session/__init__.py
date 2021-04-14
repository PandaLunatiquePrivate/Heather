import uuid
import random
import string

from org.heather.api.tools import Tools

class Session():


    @staticmethod
    def get_registry():

        return SessionRegistry


    def __init__(self, remote, profile_uid, cache={}):

        self._remote = remote.strip()
        self._profileUid = profile_uid
        self._cache = cache
        self._session_token = str(uuid.uuid4())
        self._session_key = Tools.get_uid(64)


    def get_remote(self):

        return self._remote

    
    def set_remote(self, remote):

        self._remote = remote


    def get_session_token(self):

        return self._session_token


    def get_session_key(self):

        return self._session_key


    def get_profile_uid(self):

        return self._profileUid

    
    def set_profile_uid(self, profile_uid):

        self._profileUid = profile_uid


    def get_cache(self):

        return self._cache

    
    def update_cache(self, key, value):

        self._cache[key] = value


    def clear_cache(self):

        self._cache = {}
    


class SessionRegistry():

    SESSIONS = {}


    @staticmethod
    def add(sessions):

        if isinstance(sessions, Session):

            SessionRegistry.SESSIONS[sessions.get_remote()] = sessions

        elif isinstance(sessions, list):

            for s in sessions:

                SessionRegistry.SESSIONS[s.get_remote()] = s


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
    def find_session_by_profile_uid(profile_uid):

        for s in SessionRegistry.SESSIONS:

            if SessionRegistry.SESSIONS[s].get_profile_uid() == profile_uid:

                return SessionRegistry.SESSIONS[s]

        return None