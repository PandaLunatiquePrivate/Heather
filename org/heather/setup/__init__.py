import enum
import json
import os
import requests
import yaml
import sqlite3

from org.heather.api.log import Log, LogLevel


@enum.unique
class VerifyResult(enum.Enum):

    OK = 0
    NEED_SETUP = 1
    NEED_REPAIR = 2


class Setup():

    @staticmethod
    def verify(installationPath):
        print('')

    @staticmethod
    def is_config_valid(path):

        full_path = os.path.abspath(path + "heather.conf" if path.endswith('/') else path + "/heather.conf")
        print(full_path)
        if os.path.exists(full_path):

            with open(full_path, 'r') as f:

                try:

                    temp = json.load(f)
                    del temp

                    #add field verification

                    return True

                except:

                    return False

        else:
            return False


    @staticmethod
    def wizard(rootPath):

        Log.do(LogLevel.ALL, 'Launching Heather setup wizard...', up_spacing=1, bottom_spacing=1)

        Log.do(LogLevel.INFO, f'Please specify an valid installation path:\nCurrently in {rootPath}', up_spacing=1, bottom_spacing=1)

        while True:

            setupParentPath = os.path.normpath(rootPath + '\\' + input('Installation path: '))
            
            if len(setupParentPath) > 0 and os.path.isdir(setupParentPath):
                setupParentPath = os.path.abspath(setupParentPath)
                if os.access(setupParentPath, os.W_OK):
                    break
                else:
                    Log.do(LogLevel.ERROR, 'Permission denied! Can access to the specified directory! (Writting or reading)', up_spacing=1)
            else:
                Log.do(LogLevel.ERROR, 'Invalid directory!', up_spacing=1)
            
            Log.do(LogLevel.INFO, 'Please specify an valid installation path:')

        Log.do(LogLevel.INFO, 'Downloading locales files...', up_spacing=1)

        data = requests.get('https://pastebin.com/raw/48kzz6Y9')
        locales = yaml.load(data.text, Loader=yaml.CLoader)
        
        Log.do(LogLevel.GOOD, f'Found {len(locales)} locales availables!')

        Log.do(LogLevel.INFO, f'Select a default language:', up_spacing=1)

        while True:

            for locale in locales:

                Log.do(LogLevel.ALL, f'- {locale}')

            setupLocale = input('Locale language: ')

            if len(setupLocale) > 0 and locales.get(setupLocale) != None:
                break
            else:

                Log.do(LogLevel.ERROR, 'Invalid locale!', up_spacing=1)

            Log.do(LogLevel.INFO, f'Select a default language:')

        Log.do(LogLevel.INFO, f'Start automatic setup...', up_spacing=1)

        directories = [
            os.path.normpath(setupParentPath + "/avatars"), 
            os.path.normpath(setupParentPath + "/databases"),
            os.path.normpath(setupParentPath + "/locales"),
            os.path.normpath(setupParentPath + "/logs")
        ]

        for directory in directories:

            Log.do(LogLevel.ALL, f'Creating directory {directory}', delay=0.1)
            #os.mkdir(directory)

        Log.do(LogLevel.ALL, f'Setting up database...', delay=0.1)
        database = sqlite3.connect(os.path.normpath(setupParentPath + "/databases/database.db"))

        Log.do(LogLevel.ALL, f'Creating tables...', delay=0.1)
        
        queries = [
            'CREATE TABLE profiles (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, NAME VARCHAR(32) NOT NULL UNIQUE DEFAULT "New profile", PIN VARCHAR(4) NOT NULL DEFAULT "0000");',
            'CREATE TABLE movies (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, NAME VARCHAR(32) NOT NULL UNIQUE DEFAULT "New profile", PIN VARCHAR(4) NOT NULL DEFAULT "0000");'
        ]

        for query in queries:
            database.execute(query)

        database.commit()

        

            