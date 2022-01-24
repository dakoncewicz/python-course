# -*- coding: utf-8 -*-

"""
@author: Dariusz Koncewicz
@email: d.koncewicz@sdacademy.pl
@site: www.dariuszkoncewicz.pl
"""

class A:
    
    def metoda(self):
        print('Metoda z klasy A')
        
class B(A):
    
    pass

class C(A):
    
    pass

class D(B, C):
    
    pass
        
# %%
d = D()
d.metoda()        