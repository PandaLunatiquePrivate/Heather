import json
import enum
import ffmpeg


class FileDiscoverer():


    def __init__(self, directories=[]):

        self.directories = directories

    
    def discover(self):

        analysis_result = {}

        for directory in self.directories:

            print(directory)


discoverer = FileDiscoverer(directories=[])