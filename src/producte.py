#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module *producte*
=================

Bàsicament, la classe Producte retorna el str del producte mateix
'''

class Producte(object):
    """
    docstring for Product.

    >>> Producte('orange').producte
    'orange'
    >>> Producte('BanAna').producte
    'BanAna'
    >>> Producte('salt').producte
    'salt'


    """

    def __init__(self, producte):
        self.producte = producte

if __name__ == "__main__":

    print Producte('lemon').producte

    p = Producte('lemon')
    q = Producte('banana')
    n = Producte('fanta')

    print q.producte, p.producte, n.producte
