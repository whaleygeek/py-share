# share_test.py  17/04/2016  D.J.Whale
#
# Test the generic share mechanism

import share
import time


def tx(i=""):
    data = "data %s" % str(i)
    print(data)
    share.face(data)


def rx():
    if share.isFace():
        d = share.getFace()
        print(d)


def test():
    for i in range(10):
        tx(i)
        rx()
        time.sleep(0.5)


def test_tx():
    for i in range(10):
        tx(i)
        time.sleep(0.5)


def test_rx():
    while True:
        rx()
        time.sleep(0.5)


if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        test()
    else:
        mode = sys.argv[1]
        if mode == "tx":
            test_tx()
        elif mode == "rx":
            test_rx()

# END
