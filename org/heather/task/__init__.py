import sys
import time
import random
import string
import threading


class PeriodicTask(threading.Thread):


    REGISTRY = {}


    @staticmethod
    def new(function, period=60):

        uid = PeriodicTask.gen_task_id()

        new = PeriodicTask(function, period)
        PeriodicTask.REGISTRY[uid] = new

        new.start()

        return uid


    @staticmethod
    def gen_task_id(size=16):
        
        r = ''

        for i in range(size):

            r += random.choice(string.ascii_letters + string.digits)

        return r

    
    @staticmethod
    def get_registry():

        return PeriodicTask.REGISTRY


    @staticmethod
    def find_task_by_uid(uid):

        return PeriodicTask.REGISTRY.get(uid)

    @staticmethod
    def terminate_all():

        for uid in PeriodicTask.REGISTRY:

            PeriodicTask.REGISTRY[uid].terminate()


    def __init__(self, function, period=60):

        self.function = function
        self.period = period
        self.running = True

        threading.Thread.__init__(self)


    def run(self):

        while True:
            
            if self.running:

                self.function()

                time.sleep(self.period)

            else:

                sys.exit(-1)


    def terminate(self):

        self.running = False
        sys.exit(-1)