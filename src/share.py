# share.py  17/04/2016  D.J.Whale
#
# A simple cross-process pub-sub mechanism.

def trace(msg):
    print(str(msg))


class Share():

    def __init__(self, mod):
        self.mod = mod


    def send(self, name, data=None):
        trace("send:%s=%s" % (name, data))
        # if file exists
            # wait for file to not exist
        # create the file
        # if there is data
            # write data to the file
        # close the file


    def check(self, name, wait=False):
        trace("check:%s" % name)
        # if file exists
            # return True
        # else if wait
            # wait for file to exist
            # return True
        # returl False
        return False


    def get(self, name, wait=False):
        trace("wait:%s" % name)
        # if wait
            # wait for file to exist
        # if file exists
            # open file
            # read contents into string variable
            # close file
            # delete file
            # return string
        # else
            # return None
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
