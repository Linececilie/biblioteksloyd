# encoding=utf-8
from __future__ import print_function
import random
import binascii
import time

def say(lines):
    for line in lines:
        print('{:^60}'.format(line))
        time.sleep(0.7 + random.random() * 1.3)  # always the sleep

beginning = open('README.md').read().splitlines()
beginning = [line for line in beginning if line is not '' and not line.startswith('#')]
random.shuffle(beginning)

continuation = [binascii.unhexlify(x).decode('utf-8') for x in ['416e64207468656e3f',
                '436c696e6720746f20746865206372616e653f',
                '466f6c6c6f77207468652068656172743f',
                '43756c7469766174652074686520636f64696e6720626c6f636b3f',
                '4d61646e657373',
                '416e64207965742e2e2e']]

say(beginning + continuation)
