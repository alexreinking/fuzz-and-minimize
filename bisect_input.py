#!/usr/bin/env python3

import functools
import os
import subprocess
import sys

def make_tester(encode, decode, text):
    @functools.lru_cache()
    def tester(n):
        my_text = text[:n].encode()

        enc = subprocess.run(encode, shell=True, stdout=subprocess.PIPE, input=my_text)
        if enc.returncode != 0:
            return False

        dec = subprocess.run(decode, shell=True, stdout=subprocess.PIPE, input=enc.stdout)
        return my_text == dec.stdout

    return tester

def search(encode, decode, bad_input):
    with open(bad_input) as f:
        text = f.read()

    tester = make_tester(encode, decode, text)

    lo = 0
    hi = len(text)

    lo_good = tester(lo)
    hi_good = tester(hi)

    if lo_good and hi_good:
        raise Exception('input is always good')

    while lo + 1 != hi:
        mid = lo + (hi - lo) // 2
        mid_good = tester(mid)

        if lo_good and mid_good:
            lo, lo_good = mid, mid_good
        elif not mid_good and not hi_good:
            hi, hi_good = mid, mid_good
        else:
            raise Exception('something went wrong')

    return text[:hi]

def main():
    try:
        encode, decode, bad = tuple(sys.argv[1:])
    except Exception as e:
        print('Usage: {0} <encode-cmd> <decode-cmd> <bad-input>'.format(sys.argv[0]), file=sys.stderr)
        return 1

    try:
        point = search(encode, decode, bad)
        print(point, end="")
        return 0
    except Exception as e:
        print('Error: {0}'.format(e), file=sys.stderr)
        return 1

if __name__ == '__main__':
    sys.exit(main())
