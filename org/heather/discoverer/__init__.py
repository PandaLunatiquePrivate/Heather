import os
import re
import json
import enum
import ffmpeg

import org.heather.api.enums as enums


class FileDiscoverer():


    REGISTRY = []


    def __init__(self, directories=[]):

        self.directories = directories

    
    def discover(self):

        FileDiscoverer.REGISTRY = []

        analysis_result = []

        for directory in self.directories:

            if directory['recursive']:

                analysis_result.extend(FileDiscoverer._recursive(directory['path']))

            else:

                analysis_result.extend(FileDiscoverer._single(directory['path']))

        return analysis_result

    
    @staticmethod
    def _recursive(path):

        result = []

        for file in os.listdir(path):

            relative_path = path + '/' + file
            abs_path = os.path.normpath(os.path.abspath(relative_path))

            if os.path.isfile(relative_path):

                if abs_path not in FileDiscoverer.REGISTRY:

                    file_type = enums.FileExtensions.is_supported(abs_path)

                    if isinstance(file_type, enums.FileType):

                        FileDiscoverer.REGISTRY.append(abs_path)

                        data = {
                            'file_name': file, 
                            'type': file_type, 
                            'relative_path': relative_path, 
                            'absolute_path': abs_path
                        }
                        result.append(data)

            else:

                result.extend(FileDiscoverer._recursive(relative_path))
            

        return result
    

    @staticmethod
    def _single(path):

        result = []

        for file in os.listdir(path):

            relative_path = path + '/' + file
            abs_path = os.path.normpath(os.path.abspath(relative_path))

            if abs_path not in FileDiscoverer.REGISTRY:

                file_type = enums.FileExtensions.is_supported(abs_path)

                if isinstance(file_type, enums.FileType):

                    FileDiscoverer.REGISTRY.append(abs_path)

                    data = {
                        'file_name': file, 
                        'type': file_type, 
                        'relative_path': relative_path, 
                        'absolute_path': abs_path
                    }
                    result.append(data)

        return result


class FileParser():


    @staticmethod
    def parse(name):

        data = {}

        result = re.match(r'^((([a-zA-Z0-9_\-$ ]+)([sS]([0-9]+)[eE]([0-9]+)))\.([a-zA-Z0-9]+))$', name)

        if result == None:
            
            result = re.match(r'^(([a-zA-Z0-9_\-$ ]+)\.([a-zA-Z0-9]+))$', name)

            if result != None:

                data['raw_file_name'] = name
                data['file_name'] = result.group(2)
                data['type'] = 'movie'
                data['raw_movie_name'] = result.group(2)
                data['movie_name'] = result.group(2).replace('-', '').replace('_', '').strip()
                data['extension'] = result.group(3)

        else:

            data['raw_file_name'] = name
            data['file_name'] = result.group(2)
            data['type'] = 'serie'
            data['raw_serie_name'] = result.group(3)
            data['serie_name'] = result.group(3).replace('-', '').replace('_', '').strip()
            data['raw_season_episode'] = result.group(4)
            data['season'] = int(result.group(5))
            data['episode'] = int(result.group(6))
            data['extension'] = result.group(7)

        return data