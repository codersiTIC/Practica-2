#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Module *recepta*
================
'''

from producte import*
from string import*


class Recepta(object):
    """docstring for Recepta."""

    def __init__(self, nom):
        self.nom = nom
        self._ingredients = []

    def afegeix_ingredient(self, p,q):
        '''
        Modificador. Afegeix q grams del producte p a la recepta\n
        Si la recepta ja contenia el Producte p, incrementa la seva quantitat en q grams.

            :param p: Producte
            :type p: str
            :returns:

        >>> r = Recepta('Pastís Xocolata')
        >>> r.afegeix_ingredient('Llet', 150)
        [('Llet', 150)]
        >>> r.afegeix_ingredient('xocolata', 200)
        [('Llet', 150), ('xocolata', 200)]
        >>> r.afegeix_ingredient('xocolata', 200)
        [('Llet', 150), ('xocolata', 400)]
        '''
        i = 0
        for element in self._ingredients:
            if element[0] == p:
                j = element[1]
                i = self._ingredients.index(element)

        if i != 0:
            del self._ingredients[i]
            self._ingredients.append((Producte(p).producte, q + j))

        else:
            self._ingredients.append((Producte(p).producte,q))

        return self._ingredients
        
    def conte_ingredient(self,p):
        '''
        Donat un producte, retorna True si està dins la recepta

        >>> suc = Recepta('suc')
        >>> suc.afegeix_ingredient('taronja', 200)
        [('taronja', 200)]
        >>> suc.afegeix_ingredient('aigua', 1000)
        [('taronja', 200), ('aigua', 1000)]
        >>> suc.conte_ingredient('taronja')
        True
        >>> suc.conte_ingredient('aigua')
        True
        >>> suc.conte_ingredient('poma')
        False
        '''

        for element in self._ingredients:
            if element[0] == p:
                return True
        else:
            return False

    def quantitat_ingredient(self,p):
        '''
        -- Retorna la quantitat de producte p en grams o 0 si no en conté --

        >>> r = Recepta('Banana split')
        >>> r.afegeix_ingredient('Banana', 200)
        [('Banana', 200)]
        >>> r.afegeix_ingredient('Xocolata', 100)
        [('Banana', 200), ('Xocolata', 100)]
        >>> r.quantitat_ingredient('Banana')
        200
        >>> r.quantitat_ingredient('Blueberry')
        0
        >>> r.quantitat_ingredient('Xocolata')
        100
        '''
        for element in self._ingredients:
            if element[0] == p:
                return element[1]

        else:
            return 0


    def pes_total(self):
        '''
        -- Retorna el pes base total de la recepta en grams --


        >>> llimonada = Recepta('llimonada')
        >>> llimonada.afegeix_ingredient('Llimona', 50)
        [('Llimona', 50)]
        >>> llimonada.afegeix_ingredient('Aigua', 1000)
        [('Llimona', 50), ('Aigua', 1000)]
        >>> llimonada.pes_total()
        1050
        '''

        return sum([tupla[1] for tupla in self._ingredients])


    def ingredients(self):
        '''
        -- Retorna la llista d'ingredients --

        >>> llimonada = Recepta('llimonada')
        >>> llimonada.afegeix_ingredient('Llimona', 50)
        [('Llimona', 50)]
        >>> llimonada.afegeix_ingredient('Aigua', 1000)
        [('Llimona', 50), ('Aigua', 1000)]
        >>> llimonada.ingredients()
        ['Llimona', 'Aigua']
        >>> llimonada.afegeix_ingredient('Sucre', 50)
        [('Llimona', 50), ('Aigua', 1000), ('Sucre', 50)]
        >>> llimonada.ingredients()
        ['Llimona', 'Aigua', 'Sucre']
        '''

        return [tupla[0] for tupla in self._ingredients]
