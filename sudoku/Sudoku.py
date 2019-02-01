# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 19:25:08 2019

@author: Ivan Alves
"""

from Grafo import Grafo

if __name__ == "__main__":

    output_file_name = ""
    input_file = open("sudoku_trabalho.txt","r")
    celulas = ""
    for linha in input_file:
        celulas = celulas + ((linha.replace("\n","").replace(".","N")))
    celulas = list(celulas)
    Grafo = Grafo(celulas)
    Grafo.solucao(output_file_name)
    Grafo.escreveArquivo("resultado_sudoku_trabalho.txt")
    
