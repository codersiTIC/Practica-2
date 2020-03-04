'''
el mòdul receptari.py conté la classe Receptari. La classe ha de tenir els següents atributs:
receptes [dict, Privat] És un diccionari en el que la clau correspon al nom de totes les receptes
del receptari i el valor correspon a l’objecte Recepta corresponent.
productes [dict, Privat] És un diccionari en el que la clau correspon al nom de tots els productes
que intervenen en el receptari i el valor correspon a l’objecte Producte corresponent.
La classe disposarà dels següents mètodes:
1.
init (self)
Constructor. Crea un receptari buit, sense productes ni receptes.
2. afegeix recepta(self,n)
Modificador. Afegeix una recepta de nom n al receptari. Si existia una recepta del mateix
nom es queixa. La recepta, inicialment no té ingredients.
3. afegeix producte(self, nomp)
Afegeix un nou Producte de nom nomp. Si el producte ja existeix es queixa.
4. afegeix ingredient recepta(self,nomr, nomp, q)
Afegeix q grams de l’ingredient de nom nomp a la recepta de nom nomr. Si la recepta o
l’ingredient no existeix es queixa.
5. receptes ingredient(self,nomp)
Retorna la llista de noms de receptes en que participa l’ingredient de nom nomp.
6. receptes(self)
Retorna la llista de noms de receptes del receptari.
7. ingredients(self)
Retorna la llista de noms de productes del receptari.
8. recepta(self,nomr)
Retorna una llista de parells (nomp, q) cadascun dels quals representa un ingredient de la
recepta nomr. Cada parell agrega el nom del producte nomr i el pes necessari en grams q.
'''

class Receptari(object):
    def __init__(self, receptes, productes):
        self.receptes = receptes
        self.productes = productes
de

    def
