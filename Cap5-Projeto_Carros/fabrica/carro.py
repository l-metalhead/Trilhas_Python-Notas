#!usr/bin/env python3.6
# -*- coding: UTF-8 -*-

"""
Modulo contendo construtor de Carros
"""

class Carro(object):
    def __init__(self, cor, potencia):
        self.cor = cor
        self.potencia = potencia
        self.velocidade = 0

    def __atualiza_velocidade(self, valor):
        self._velocidade = valor

    def acelar(self):
        self.__atualiza_velocidade(valor=10)
        print("Vrruuum!!!")

    def freiar(self):
        self.__atualiza_velocidade(valor=0)
        print("Parando!!!")
