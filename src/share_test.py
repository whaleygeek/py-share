# share_test.py  17/04/2016  D.J.Whale
#
# Test the generic share mechanism

import share
import time


def tx():
    share.face("happy")


def rx():
    if share.isFace():
        f = share.getFace()
        print(f)


def test():
    for i in range(10):
        tx()
        rx()
        time.sleep(0.5)


def test_tx():
    for i in range(10):
        tx()
        time.sleep(0.5)


def test_rx():
    for i in range(10):
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
