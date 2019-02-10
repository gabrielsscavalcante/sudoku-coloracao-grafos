# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:23:08 2019

@author: Ivan Alves
"""


class Vertice:
    def __init__(self,indice,valor):
        self.indice = indice
        self.valor = valor
        self.adjacentes = []
        self.grauSaturacao = 0
        self.grau = 0

    def calculaSaturacao(self):
        for adjacente in self.adjacentes:
            if adjacente.getvalor() != "N":
                self.grauSaturacao += 1

    def getvalor(self):
        return self.valor

    def setvalor(self,valor):
        self.valor = valor

    def aumentaSaturacao(self):
        self.grauSaturacao += 1

    def diminuiSaturacao(self):
        self.grauSaturacao += 1

    def getSaturacao(self):
        return self.grauSaturacao

    def addAdjacente(self,vertice):
        self.adjacentes.append(vertice)
        self.grau += 1

    def cores(self,ordem):
        possibilidades = list(range(1,ordem+1))
        setPossibilidades = set(possibilidades)
        jaExiste = set()
        for adjacente in self.adjacentes:
            if adjacente.getvalor() == "N":
                continue
            jaExiste.add(int(adjacente.getvalor()))
        setPossibilidades = setPossibilidades - jaExiste
        if (len(setPossibilidades) == 0):
            return -1
        return list(setPossibilidades)

    def aumentaSaturacaoAdjacentes(self):
        for adjacente in self.adjacentes:
            adjacente.aumentaSaturacao()

    def diminuiSaturacaoAdjacentes(self):
        for adjacente in self.adjacentes:
            adjacente.diminuiSaturacao()