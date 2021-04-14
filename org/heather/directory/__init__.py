from org.heather.database import Database


class Directory():


    DIRECTORIES = {}


    @staticmethod
    def add_directory(directory):

        Directory.DIRECTORIES[directory.get_directory_uid()] = directory
    

    @staticmethod
    def get_directories():

        return Directory.DIRECTORIES

    
    @staticmethod
    def find_directory_by_uid(directory_uid):

        return Directory.DIRECTORIES.get(directory_uid.strip())

    
    @staticmethod
    def clear_directories():

        Directory.DIRECTORIES = {}


    @staticmethod
    def update_directories():

        directories = Database.get_directories()
        
        for d in directories:

            newDirectory = Directory(d['id'], d['uid'], d['name'], d['path'], d['is_recursive'])
            Directory.add_directory(newDirectory)


    def __init__(self, id, uid, name, path, is_recursive):

        self._id = id
        self._uid = uid
        self._name = name
        self._path = path
        self._is_recursive = is_recursive


    def get_directory_id(self):

        return self._id


    def get_directory_uid(self):

        return self._uid


    def get_directory_name(self):

        return self._name


    def get_directory_piath(self):

        return self._path


    def is_recursive(self):

        return self._is_recursive
    

