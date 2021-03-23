import random
import string

class Tools():

    @staticmethod
    def get_uid(size):

        return ''.join(random.choice(string.ascii_letters + string.digits) for i in range(size))

print(Tools.get_uid(16))