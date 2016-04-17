# share_test.py  17/04/2016  D.J.Whale
#
# Test the generic share mechanism

import share


def tx():
    share.face("happy")



def rx():
    if share.isFace():
        f = share.getFace()
        print(f)


def test():
    import time
    for i in range(10):
        tx()
        rx()
        time.sleep(0.5)


if __name__ == "__main__":
    test()

# END
