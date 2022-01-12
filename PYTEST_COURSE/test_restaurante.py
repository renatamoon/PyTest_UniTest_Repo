# -*- coding: utf-8 -*-
import pytest

from restaurante import Restaurante

"""PRIMEIRO TESTE - teremos um restaurante que tem pedidos na fila. Esse teste deve assegurar
que quando o restaurante iniciar com os pedidos, ele tenha 0 pedidos na fila"""


def test_pedidos_na_fila_valor_inicial_padrao_igual_a_zero():
    restaurante = Restaurante("Pizzaria X")
    assert restaurante.pedidos_na_fila == 0


def test_pedidos_na_fila_valor_inicial_maior_que_zero():
    restaurante = Restaurante("Pizzaria X", 1)
    assert restaurante.pedidos_na_fila == 1


"""TESTE 3 - verifica se o teste não tem numeros negativos. Porque o restaurante não
pode ter -1 ou mais pedidos negativos."""


def test_pedidos_na_fila_valor_inicial_menor_que_zero():
    with pytest.raises(ValueError):
        Restaurante("Pizzaria X", -1)


"""TESTE 4 - ELE TESTA O METODO adiciona_pedido PARA VER SE ESTÁ FUNCIONANDO"""
def test_adiciona_um_pedido_na_fila():
    restaurante = Restaurante("Pizzaria X", 1)
    restaurante.adiciona_pedido()
    assert restaurante.pedidos_na_fila == 2


"""TESTE 5 - TESTA SE O METODO remove_pedido está correto para remover, e passa que 
o numero de pedidos deve ser igual a 0"""


def test_remove_um_pedido_na_fila():
    restaurante = Restaurante("Pizzaria X", 1)
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0

"""TESTE 6 - verificar se o metodo remove_pedido faz com que a fila de pedidos não
seja negativa"""


def test_remove_um_pedido_na_fila_vazia():
    restaurante = Restaurante("Pizzaria X")
    restaurante.remove_pedido()
    assert restaurante.pedidos_na_fila == 0