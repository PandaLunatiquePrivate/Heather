import os
import json

from org.heather.api.log import Log, LogLevel


class Config():


    CONFIG = {}


    @staticmethod
    def load_config(path):

        with open(os.path.normpath(path + '\\heather.conf'), 'r') as f:

            config = json.load(f)

            pathsToVerify = [
                config['general']['parent_path'],
                config['general']['parent_path'] + '\\' + config['general']['paths']['avatars'],
                config['general']['parent_path'] + '\\' + config['general']['paths']['database'],
                config['general']['parent_path'] + '\\' + config['general']['paths']['locales'],
                config['general']['parent_path'] + '\\' + config['general']['paths']['logs'],
                config['general']['parent_path'] + '\\' + config['general']['paths']['locales'] + '\\' + config['general']['locale'] + '.lang'
            ]

            for path in pathsToVerify:
                if not os.path.exists:
                    Log.log(LogLevel.ERROR, f'Configuration path {path} is pointing to a unexistant file or directory.')
                    return False

        Config.CONFIG = config

        Config.CONFIG['parsed_paths'] = {
            'parent': os.path.abspath(os.path.normpath(config['general']['parent_path'])),
            'avatars': os.path.abspath(os.path.normpath(config['general']['parent_path'] + '\\' + config['general']['paths']['avatars'])),
            'database': os.path.abspath(os.path.normpath(config['general']['parent_path'] + '\\' + config['general']['paths']['database'])),
            'locales': os.path.abspath(os.path.normpath(config['general']['parent_path'] + '\\' + config['general']['paths']['locales'])),
            'logs': os.path.abspath(os.path.normpath(config['general']['parent_path'] + '\\' + config['general']['paths']['logs']))
        }

        return True


