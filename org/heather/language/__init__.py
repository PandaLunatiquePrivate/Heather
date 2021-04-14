import yaml
import time
import datetime


class Translations():

    CACHE = {}
    PARENT_PATH = None

    @staticmethod
    def load_in_cache(language):

        absPath = f'C:\\Users\\trist\Desktop\\Projects\\Heather\\heather_dev\\locales\\{language}.lang'
        parsedData = yaml.load(open(absPath, 'r'), Loader=yaml.Loader)

        cacheStorage = {
            'translations': parsedData,
            'cache_last_use': datetime.datetime.now()
        }

        Translations.CACHE[language] = cacheStorage

        return True


    @staticmethod
    def is_in_cache(language):

        return Translations.CACHE.get(language) != None


    @staticmethod
    def update_cache():

        _toRemove = []

        for l in Translations.CACHE:

            timeDelta = datetime.datetime.now() - Translations.CACHE[l]['cache_last_use']

            if timeDelta.total_seconds() >= 60:

                _toRemove.append(l)

        for r in _toRemove:

            del Translations.CACHE[r]
            print(f'LOG: Language deleted from cache: {r}')


    @staticmethod
    def from_key(language, key):

        if not Translations.is_in_cache(language):
            Translations.load_in_cache(language)
        else:
            Translations.CACHE[language]['cache_last_use'] = datetime.datetime.now()

        translation = Translations.CACHE[language]['translations'].get(key)

        return translation if translation != None else key

    
    @staticmethod
    def gen_translator(language):

        return lambda key: Translations.from_key(language, key)


    @staticmethod
    def clear_cache():

        Translations.CACHE = {}