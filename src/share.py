# share.py  17/04/2016  D.J.Whale
#
# A simple cross-process pub-sub mechanism.

import os
import time

#TODO what about locking?


def trace(msg):
    print(str(msg))

EXTN      = ".share"
POLL_RATE = 0.5

class Share():

    def __init__(self, mod):
        self.mod = mod


    def send(self, name, data=None):
        trace("send:%s=%s" % (name, data))
        name += EXTN

        # wait for file to not exist
        while os.path.isfile(name):
            time.sleep(POLL_RATE)

        # create file and write optional data to it
        f = open(name, "w")
        if data != None:
            f.write(data)
        f.close()


    def check(self, name, wait=False):
        trace("check:%s" % name)
        name += EXTN

        if os.path.isfile(name):
            return True

        elif wait:
            while not os.path.isfile(name):
                time.sleep(POLL_RATE)
            return True

        return False


    def get(self, name, wait=False):
        trace("wait:%s" % name)
        name += EXTN
        if wait:
            while not os.path.isfile(name):
                time.sleep(POLL_RATE)

        if os.path.isfile(name):
            f = open(name, 'r')
            data = f.read()
            f.close()
            os.unlink(name)
            return data
        else:
            return None


    def __repr__(self):
        return "Share"


    def __dir__(self):
        return []


    def __getattr__(self, name):
        if name.startswith("is"):
            name = name[2:]
            print("build a checker for: %s" % name)
            def fn():
                return self.check(name)

        elif name.startswith("get"):
            name = name[3:]
            print("build a getter for:%s" % name)
            def fn():
                return self.get(name)

        else:
            print("build a sender for:%s" % name)
            def fn(data=None):
                return self.send(name, data)

        return fn


import sys
sys.modules[__name__] = Share(sys.modules[__name__])
