#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
El mòdul receptari.py conté la classe Receptari. La classe ha de tenir els següents atributs:
_receptes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de totes les _receptes
    del receptari i el valor correspon a l’objecte Recepta corresponent.

productes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de tots els productes
    que intervenen en el receptari i el valor correspon a l’objecte Producte corresponent.
'''

from recepta import*
from string import*

class Receptari(object):

    def __init__(self):
        self._receptes = dict()
        self._productes = dict()


    def afegeix_recepta(self,n):
        '''
        Modificador. Afegeix una recepta de nom n al receptari. Si existia una recepta del mateix
        nom es queixa.
        La recepta, inicialment no té ingredients.

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_recepta('Pastís Xocolata')
        >>> Receptari.afegeix_recepta('Pastís Xocolata')
        La recepta ja existeix
        >>> Receptari.afegeix_recepta('Gofres')
        '''

        if self._receptes.has_key(n):
            print "La recepta ja existeix"
        else:
            self._receptes[n] = Recepta(n)


    def afegeix_producte(self, nomp):
        '''
        Afegeix un nou Producte de nom nomp. Si el producte ja existeix es queixa.

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Farina')
        El producte ja existeix
        '''

        if nomp in self._productes.keys():
            print "El producte ja existeix"
        else:
            self._productes[nomp] = Recepta(nomp)


    def afegeix_ingredient_recepta(self,nomr,nomp,q):
        '''
        Afegeix q grams de l’ingredient de nom nomp a la recepta de nom nomr. Si la recepta o
        l’ingredient no existeix es queixa.

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        La recepta < Gofre > no existeix
        >>> Receptari.afegeix_recepta('Gofre')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Farina')
        El producte ja existeix
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Farina', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Ous', 500)
        >>> Receptari.afegeix_ingredient_recepta('Gofre', 'Llet', 500)
        El producte < Llet > no existeix
        '''
        if (nomr not in self._receptes.keys()):
            print ("La recepta < %s > no existeix")%(nomr)
        else:
            if (nomp not in self._productes.keys()):
                print ("El producte < %s > no existeix")%(nomp)
            else:
                self._receptes[nomr].afegeix_ingredient(nomp, q)

    
    def receptes_ingredient(self,nomp):
        '''
        Retorna la llista de noms de receptes en que participa l’ingredient de nom nomp.

        >>> Receptari = Receptari()
        >>> Receptari.afegeix_producte('Farina')
        >>> Receptari.afegeix_producte('Ous')
        >>> Receptari.afegeix_producte('Llet')
        >>> Receptari.afegeix_producte('Sucre')
        '''
        l = []
        for recepta in self._receptes.values():
            if nomp in recepta.ingredients():
                l.append(recepta.nom)
        return l


    def receptes(self):
        '''
        Retorna la llista de noms de receptes del receptari.
        '''
        return self._receptes.keys()


    def ingredients(self):
        '''
        Retorna la llista de noms de _productes del receptari.
        '''
        return self._productes.keys()


    def recepta(self,nomr):
        '''
        Retorna una llista de parells (nomp, q) cadascun dels quals representa un ingredient de la
        recepta nomr. Cada parell agrega el nom del producte nomr i el pes necessari en grams q.
        '''
        return self._receptes[nomr]._ingredients
