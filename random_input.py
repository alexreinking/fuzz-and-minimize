#!/usr/bin/env python3

import functools
import os
import random
import subprocess
import sys

def make_tester(encode, decode):
    def tester(text):
        text = text.encode()

        enc = subprocess.run(encode, shell=True, stdout=subprocess.PIPE, input=text)
        if enc.returncode != 0:
            return False

        dec = subprocess.run(decode, shell=True, stdout=subprocess.PIPE, input=enc.stdout)
        return text == dec.stdout
    return tester

def fuzz(encode, decode, alphabet):
    tester = make_tester(encode, decode)

    for _ in range(100000):
        k = int(random.gauss(1000, 300))
        text = ''.join(random.choices(alphabet, k=abs(k)))
        if not tester(text):
            return text

    raise Exception('Could not find bad input!')

def main():
    try:
        encode, decode, alphabet = tuple(sys.argv[1:])
    except Exception as e:
        print('Usage: {0} <encode-cmd> <decode-cmd> <alphabet>'.format(sys.argv[0]), file=sys.stderr)
        return 1

    try:
        point = fuzz(encode, decode, alphabet)
        print(point, end="")
        return 0
    except Exception as e:
        print('Error: {0}'.format(e), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
