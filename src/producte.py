#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Producte(object):
    """
    docstring for Product.

    >>> Producte('orange').producte
    'Orange'
    >>> Producte('banana').producte
    'Banana'
    >>> Producte('salt').producte
    'Salt'


    """

    def __init__(self, producte):
        self.producte = producte.capitalize()

if __name__ == "__main__":

    print Producte('lemon').producte

    p = Producte('lemon')
    q = Producte('banana')
    n = Producte('fanta')

    print q.producte, p.producte, n.producte
