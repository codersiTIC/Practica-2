#!/usr/bin/env python
# -*- coding: utf-8 -*-
from receptari import*

class Interpret(object):
    def __init__(self):
        self._dcom = dict()
        self._prompt = str()

    def set_prompt(self,p):
        self._prompt = p

    def afegeix_ordre(self, nomc, ordre):
        '''
        Es pot afegir qualsevol cosa al diccionari, però a main farem que
        entrin funcions obligatoriament

        Modificador. Afegeix a l’intèrpret una ordre de nom nomc associada a la funció ordre. Si
        ja existia una ordre amb aquest nom, es queixa. Noteu que el tercer paràmetre del mètode
        és una funció!
        La funció de nom ordre és una funció que té com a únic paràmetre una llista de strings.
        '''
        if self._dcom.has_key(nomc):
            return 'Failed. This command already exists'
        else:
            self._dcom[nomc] = ordre



    def run(self):
        '''
        Només vàlid per funcions amb només un paràmetre com argument.
        No caldrà arreglar res, a main ho hem de tenir en compte.
        Farem que les funcions siguin amb argument obligatoriament.

        Arrenca l’execució d’aquest intèrpret d’ordres. L’intèrpret s’executa indefinidament fins
        que l’usuari escriu l’ordre surt.
        A cada cicle d’interpretació, l’intèrpret escriu el prompt, llegeix un string del teclat, l’ana-
        litza separant els mots que el formen. El primer mot considera que és un nom d’ordre i la
        resta de mots els paràmetres d’aquesta ordre. Finalment executa la funció corresponent a
        l’ordre i li passa com a paràmetre la resta de mots en una llista.
        '''
        
        while True:
            print self._prompt,
            p = raw_input()
            ll = p.split()
            ordres = ll[1:]
            '''
            print
            print ll, ll[0], ll[1:]
            print ordres
            print self._dcom
            '''

            if self._dcom.has_key(ll[0]):
                for element in ordres:
                    self._dcom[ll[0]](element)
                    #print self._dcom[ll[0]](element)
            elif ll[0] == 'surt' or ll[0] == 'Surt':
                break
