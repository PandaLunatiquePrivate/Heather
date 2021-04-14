import math
import random
import string
import datetime

class Tools():

    @staticmethod
    def get_uid(size, additionnal_charset=''):

        return ''.join(random.choice(string.ascii_letters + string.digits + additionnal_charset) for i in range(size))

    
    @staticmethod
    def convert_to_unix(d):

        result = d - datetime.datetime(1970, 1, 1)

        return math.floor(result.total_seconds())