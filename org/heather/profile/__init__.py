from org.heather.database import Database


class Profile():


    PROFILES = {}


    @staticmethod
    def add_profile(profile):

        Profile.PROFILES[profile.get_profile_uid()] = profile
    

    @staticmethod
    def get_profiles():

        return Profile.PROFILES

    
    @staticmethod
    def find_profile_by_uid(profile_uid):

        return Profile.PROFILES.get(profile_uid.strip())

    
    @staticmethod
    def clear_profiles():

        Profile.PROFILES = {}


    @staticmethod
    def update_profiles():

        profiles = Database.get_profiles()
        
        for p in profiles:

            newProfile = Profile(p['id'], p['uid'], p['group_uid'], p['name'], p['pin'])
            Profile.add_profile(newProfile)


    def __init__(self, id, uid, group_uid, name, pin):

        self._id = id
        self._uid = uid
        self._group_uid = group_uid
        self._name = name
        self._pin = pin


    def get_profile_id(self):

        return self._id


    def get_profile_uid(self):

        return self._uid


    def get_profile_group_uid(self):

        return self._group_uid


    def get_profile_name(self):

        return self._name


    def get_profile_pin(self):

        return self._pin
    

