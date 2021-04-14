import sqlite3

class Database():

    CON = None
    FIELDS_TYPING = {
        'id': '@integer',
        'uid': '@varchar',
        'name': '@varchar',
        'path': '@varchar',
        'is_recursive': '@boolean',
        'is_kid_friendly': '@boolean',
        'group_uid': '@varchar',
        'pin': '@varchar'
    }

    @staticmethod
    def connect(path):

        Database.CON = sqlite3.connect(path, check_same_thread=False)

    @staticmethod
    def get_profiles():

        res = Database.CON.execute('SELECT * FROM profiles')

        profiles = res.fetchall()

        result = []

        for profile in profiles:

            i = 0
            fetch = {}
            for field in profile:

                if Database.FIELDS_TYPING[res.description[i][0].lower()] == '@boolean':
                    fetch[res.description[i][0].lower()] = bool(field)
                else:
                    fetch[res.description[i][0].lower()] = field
                i += 1

            result.append(fetch)

        return result


    @staticmethod
    def get_directories():

        res = Database.CON.execute('SELECT * FROM directories')

        directories = res.fetchall()

        result = []

        for directory in directories:

            i = 0
            fetch = {}
            for field in directory:

                if Database.FIELDS_TYPING[res.description[i][0].lower()] == '@boolean':
                    fetch[res.description[i][0].lower()] = bool(field)
                else:
                    fetch[res.description[i][0].lower()] = field
                i += 1

            result.append(fetch)

        return result

