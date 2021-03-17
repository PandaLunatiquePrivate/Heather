import os
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
                    print(file_type)

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
                print(file_type)
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