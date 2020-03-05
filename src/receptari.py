'''
El mòdul receptari.py conté la classe Receptari. La classe ha de tenir els següents atributs:
receptes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de totes les receptes
    del receptari i el valor correspon a l’objecte Recepta corresponent.

productes [dict, Privat]
    És un diccionari en el que la clau correspon al nom de tots els productes
    que intervenen en el receptari i el valor correspon a l’objecte Producte corresponent.
'''

from recepta import*
from string import*

class Receptari(object):

    def __init__(self):
        self.receptes = dict()
        self._productes = dict()

    def afegeix_recepta(self,n):
        '''
        Modificador. Afegeix una recepta de nom n al receptari. Si existia una recepta del mateix
        nom es queixa.
        La recepta, inicialment no té ingredients.
        '''
        if self.receptes.has_key(n)):
            pass
        else:
            self.receptes[n] = Recepta(n)

    def afegeix_producte(self, nomp):
        '''
        Afegeix un nou Producte de nom nomp. Si el producte ja existeix es queixa.
        '''
        d[Producte(nomp).producte] = 0


    def afegeix_ingredient_recepta(self,nomr,nomp,q):
        '''
        Afegeix q grams de l’ingredient de nom nomp a la recepta de nom nomr. Si la recepta o
        l’ingredient no existeix es queixa.
        Afegeix q grams de l’ingredient de nom nomp a la recepta de nom nomr. Si la recepta o
        l’ingredient no existeix es queixa.
        '''
        pass


    def receptes_ingredient(self,nomp):

        '''
        Retorna la llista de noms de receptes en que participa l’ingredient de nom nomp.
        '''
        if self.receptes.has_key(nomp):
            pass

    def receptes(self):
        '''
        Retorna la llista de noms de receptes del receptari.
        '''
        for element in self.receptes:
            return self.receptes.keys()

    def ingredients(self):
        '''
        Retorna la llista de noms de productes del receptari.
        '''
        return self._ingredients.keys()

    def recepta(self,nomr):
        '''
        Retorna una llista de parells (nomp, q) cadascun dels quals representa un ingredient de la
        recepta nomr. Cada parell agrega el nom del producte nomr i el pes necessari en grams q.
        '''

        pass
