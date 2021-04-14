

class Response():

    @staticmethod
    def builder(uid, version):

        responseBuilder = {
            "meta": {
                "request_uid": uid,
                "version": version,
                "execution": None
            },
            "result": {}
        }

        return responseBuilder
