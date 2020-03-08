#!/usr/bin/env python
# -*- coding: utf-8 -*-


from receptari import*
from interpret import*

'''
El modul main.py conte el programa principal.
Aquest programa crea una inst`ancia de Receptari
i una instancia d’Interpret juntament amb les
funcions que implementen les ordres necessaries.

A continuacio, engega l’int`erpret. Aquest es va
comunicant interactivament amb l’usuari fins acabar
la sessio.

L’interpret ha de tenir les seguents ordres:

producte <nom>
    Afegeix un producte al receptari que te nom <nom>.

recepta <nom>
    Afegeix una recepta al receptari que te nom <nom>.

ingredient <nomp> <nomr> <qua>
    Afegeix <qua> grams de l’ingredient de nom <nomp> a la recepta de nom <nomr>.


print <ent> [<nom>]
    Escriu per pantalla segons el valor de <ent>. Si <ent> és:

    receptes
        Escriu la llista de noms de receptes del receptari.
    productes
        Escriu la llista de noms de producte del receptari.

        recepta
            Escriu els ingredients i la quantitat que intervenen en la recepta de nom <nom>.

        receptes-ing
            Escriu la llista de noms de recepta en les que participa l’ingredient anomenat <nom>.

    surt
    Acaba l’execució del programa.
'''

r = Receptari()
i = Interpret()




def printlist(ent = str(), nom = str()):
    if ent == 'receptes':
        print r.receptes()

    elif ent == 'productes':
        print r.ingredients()
        #print r.receptes_ingredient(nom)

    else:
        print "No has introduit cap recepta o producte"

i.set_prompt('**')

i.afegeix_ordre('producte', r.afegeix_producte)
i.afegeix_ordre('receptes', r.receptes)
i.afegeix_ordre('recepta', r.afegeix_recepta)
i.afegeix_ordre('ingredient', r.afegeix_ingredient_recepta)
i.afegeix_ordre('print', printlist)

i.run()
