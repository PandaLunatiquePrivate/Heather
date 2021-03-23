import sqlite3

class Database():

    CON = None

    @staticmethod
    def connect(path):

        Database.CON = sqlite3.connect(path)

    @staticmethod
    def get_profiles():

        res = Database.CON.execute('SELECT * FROM profiles')
        
        profiles = res.fetchall()

        result = []

        for profile in profiles:

            i = 0
            fetch = {}
            for field in profile:

                fetch[res.description[i][0].lower()] = field
                i += 1

            result.append(fetch)

        print(result)

Database.connect('C:\\Users\\trist\\Desktop\\Projects\\Heather\\heather_dev\\database\\database.db')
Database.get_profiles()