# -*- coding: utf-8 -*-

"""
@author: Dariusz Koncewicz
@email: d.koncewicz@sdacademy.pl
@site: www.dariuszkoncewicz.pl
"""

import sys


def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n - 1)


if __name__ == '__main__':
    print(silnia(int(sys.argv[1])))