# -*- coding: utf-8 -*-

"""
@author: Dariusz Koncewicz
@email: d.koncewicz@sdacademy.pl
@site: www.dariuszkoncewicz.pl
"""

def add(x, y):
    """Zwraca sumę dwóch liczb.
    
    >>> add(3, 4)
    7
    
    >>> add(2, 8)
    100
    """
    return x + y


if __name__ == '__main__':
    import doctest
    doctest.testfile('test.txt')