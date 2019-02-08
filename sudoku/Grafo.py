# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:21:29 2019

@author: Ivan Alves
"""




import math
from Vertice import Vertice


class Grafo:
    def __init__(self,celulas):
        self.numeroDeVertices = len(celulas)
        self.ordem = int(math.sqrt(self.numeroDeVertices))
        self.dimensaoQuadro = int(math.sqrt(self.ordem))
        self.vertices = self.geraVertices(celulas,self.numeroDeVertices)
        self.quadros = self.geraQuadros(self.numeroDeVertices,self.dimensaoQuadro,self.ordem)
        self.juntaAdjacentes(self.ordem)
        

    def solucao(self,output_file_name):
        if self.dSatur():
            print ("Solução encontrada e salva no arquivo de saída. ",output_file_name)
        else:
            print("Solução não encontrada")


    def geraVertices(self,celulas,numeroDeVertices):
        vertices = {}
        for i in range(numeroDeVertices):
            vertices[i] = Vertice(i,celulas[i])
        return vertices
     
    #Gera quadros de numéros  
    def geraQuadros(self,numeroDeVertices,dimensaoQuadro,ordem):
        listaQuadros = []
        for primeiroQuadroVertical in range (0,numeroDeVertices,dimensaoQuadro*ordem):
            for primeiroQuadroHorizontal in range(primeiroQuadroVertical, primeiroQuadroVertical+ordem, dimensaoQuadro):
                quadro = set()
                for vertical in range(primeiroQuadroHorizontal,primeiroQuadroHorizontal + ordem*dimensaoQuadro-1,ordem):
                    for horizontal in range(vertical,vertical+dimensaoQuadro):
                        quadro.add(horizontal)
                listaQuadros.append(quadro)
        return listaQuadros

    # Pega os adjacentes por linha  
    def linhaAdjacentes(self,indice,ordem):
        mod = indice % ordem
        dif = ordem - mod
        lim = indice + dif

        adjacentes = set()
        for i in range(indice-mod,lim):
            adjacentes.add(i)
        return adjacentes

     # Pega os adjacentes por coluna
    def colunaAdjacentes(self,indice,ordem):
        adjacentes = set()
        for subindo in range(indice,0,-ordem):
            adjacentes.add(subindo)
        for descendo in range(indice,self.numeroDeVertices,ordem):
            adjacentes.add(descendo)
        return adjacentes
    
    #Pega os adjacentes por quadro 
    def quadroAdjacentes(self,indice):
        for quadro in self.quadros:
            if indice in quadro:
                return quadro

    def juntaAdjacentes(self,ordem):
        for vertice in self.vertices:
            linhaAdjacentes = self.linhaAdjacentes(vertice,ordem)
            colunaAdjacentes = self.colunaAdjacentes(vertice,ordem)
            quadroAdjacentes = self.quadroAdjacentes(vertice)
            adjacentes = linhaAdjacentes | colunaAdjacentes | quadroAdjacentes
            self.atribuiAdjacentes(vertice,adjacentes)

    def atribuiAdjacentes(self,vertice,adjacentes):
        for adjacente in adjacentes:
            if (vertice != adjacente):
                self.vertices[vertice].setAdjacente(self.vertices[adjacente])
        self.vertices[vertice].calculaSaturacao()

    def maiorSaturacao(self):
        maiorSaturacao = 0
        maiorIndice = 0
        for vertice in self.vertices:
            if self.vertices[vertice].getSaturation() > maiorSaturacao and self.vertices[vertice].getvalor() == "N":
                maiorSaturacao = self.vertices[vertice].getSaturation()
                maiorIndice = vertice
        return maiorIndice  

    def todasCores(self):
        for vertice in self.vertices:
            if self.vertices[vertice].getvalor() == "N":
                return False
        return True

    def dSatur(self):
        if self.todasCores():
            return True
        maiorSaturacao = self.maiorSaturacao()
        coresPossiveis = self.vertices[maiorSaturacao].coresPossiveis(self.ordem)
        if coresPossiveis == -1:
            return False
        if not coresPossiveis:
            return False
        for cor in coresPossiveis:
            self.vertices[maiorSaturacao].setvalor(cor)
            self.vertices[maiorSaturacao].aumentaSaturacaoAdjacentes()
            if self.dSatur():
                return True
            else:
                self.vertices[maiorSaturacao].diminuiSaturacaoAdjacentes()
                self.vertices[maiorSaturacao].setvalor("N")
        return False

    def escreveArquivo(self, output_file_name):
        output_file = open(output_file_name, "w+")
        for vertices in self.vertices:                
            if(vertices % self.ordem == 0 and vertices != 0):
                print("",file=output_file)
            print(self.vertices[vertices].getvalor(),"",end="",file=output_file)
