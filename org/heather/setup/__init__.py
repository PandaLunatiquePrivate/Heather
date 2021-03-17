import enum
import json
import os


@enum.unique
class VerifyResult(enum.Enum):

    OK = 0
    NEED_SETUP = 1
    NEED_REPAIR = 2


class Setup():

    @staticmethod
    def verify(installation_path):
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
    def wizard():

        print('starting wizard')