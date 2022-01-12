# -*- coding: utf-8 -*-
"""Classe para testagem"""

class Restaurante:
    def __init__(self, nome, pedidos_na_fila=0):
        self.nome = nome
        if pedidos_na_fila >= 0:
            self.pedidos_na_fila = pedidos_na_fila
        else:
            raise ValueError(
                "A QUANTIDADE DE PEDIDOS NA FILA NÃO DEVE SER NEGATIVA"
            )


    def adiciona_pedido(self):
        self.pedidos_na_fila += 1


    def remove_pedido(self):
        if self.pedidos_na_fila > 0:
            self.pedidos_na_fila -= 1

