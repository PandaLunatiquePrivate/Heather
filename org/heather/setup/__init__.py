import enum
import json
import os
import requests
import yaml
import sqlite3
import traceback

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
        
        # Setup: Directories
        directories = [
            os.path.normpath(setupParentPath + "/avatars"), 
            os.path.normpath(setupParentPath + "/databases"),
            os.path.normpath(setupParentPath + "/locales"),
            os.path.normpath(setupParentPath + "/logs")
        ]

        for directory in directories:

            Log.do(LogLevel.ALL, f'Creating directory {directory}', delay=0.1)
            try:
                os.mkdir(directory)
            except:
                pass
        
        # Setup: Database
        Log.do(LogLevel.ALL, f'Setting up database...', delay=0.1)
        database = sqlite3.connect(os.path.normpath(setupParentPath + "/databases/database.db"))

        Log.do(LogLevel.ALL, f'Creating tables...', delay=0.1)
        
        queries = [
            'CREATE TABLE profiles (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, NAME VARCHAR(32) NOT NULL UNIQUE DEFAULT "New profile", PIN VARCHAR(4) NOT NULL DEFAULT "0000")',
            'CREATE TABLE movies (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, TITLE VARCHAR(64) NOT NULL DEFAULT "Unknown", TRAILER_LINK VARCHAR(256), RELEASE_DATE VARCHAR(64), GENRE TEXT, DURATION INTEGER, REAL_DURATION INTEGER, RATING REAL, POPULAR_QUOTE TEXT, SYNOPSIS TEXT, COUNTRY VARCHAR(128), PRODUCTION TEXT, DIRECTOR TEXT, CASTS TEXT, ORIGINAL_VERSION VARCHAR(16) NOT NULL, FILE_PATH VARCHAR(256), QUALITY VARCHAR(32))',
            'CREATE TABLE series (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, TITLE VARCHAR(64) NOT NULL DEFAULT "Unknown", EPISODES INTEGER, EPISODE_NAME VARCHAR(32) DEFAULT "EPISODE", SEASONS INTEGER, SEASON_NAME VARCHAR(32) DEFAULT "SEASON", TRAILERS_LINK VARCHAR(256), RELEASES_DATE VARCHAR(64), GENRE TEXT, TOTAL_DURATION INTEGER, RATING REAL, POPULAR_QUOTE TEXT, SYNOPSIS TEXT, COUNTRY VARCHAR(128), PRODUCTION TEXT, DIRECTOR TEXT, CASTS TEXT,  ORIGINAL_VERSION VARCHAR(16) NOT NULL)',
            'CREATE TABLE seasons (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, SERIE_UID VARCHAR(16) NOT NULL, SEASON INTEGER, SEASON_TITLE VARCHAR(64) NOT NULL DEFAULT "Unknown", RELEASES_DATE VARCHAR(64), TOTAL_DURATION INTEGER, POPULAR_QUOTE TEXT, SYNOPSIS TEXT, PRODUCTION TEXT, DIRECTOR TEXT, CASTS TEXT, ORIGINAL_VERSION VARCHAR(16) NOT NULL)',
            'CREATE TABLE episodes (ID INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL, UID VARCHAR(16) NOT NULL UNIQUE, SEASON_UID VARCHAR(16) NOT NULL, EPISODE INTEGER, EPISODE_TITLE VARCHAR(64) NOT NULL DEFAULT "Unknown", RELEASES_DATE VARCHAR(64), DURATION INTEGER, SYNOPSIS TEXT, CASTS TEXT, FILE_PATH VARCHAR(256), QUALITY VARCHAR(32))'
        ]

        for query in queries:
            database.execute(query)
            Log.do(LogLevel.ALL, 'Creating a table...')
            Log.do(LogLevel.COMMON, f'> {query}', delay=0.1)

        database.commit()

        # Setup: Download locales
        Log.do(LogLevel.ALL, f'Downloading locales...', delay=0.1)

        for locale in locales:

            Log.do(LogLevel.ALL, f'Downloading {locale}.lang file...', delay=0.1)

            try:
            
                data = requests.get(locales[locale]).content
                with open(os.path.normpath(setupParentPath + f"/locales/{locale}.lang"), 'wb+') as f:

                    f.write(data)

                Log.do(LogLevel.GOOD, f'Downloaded {locale}.lang!', delay=0.05)

            except:

                Log.do(LogLevel.WARN, f'Can\'t download {locale}.lang!', delay=0.05)



        

            