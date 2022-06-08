# -*- coding: utf-8 -*-
import pytest


#função que será testada
def soma_1(numero):
    return int(numero) + 1


#codigo de teste 1 para testar a função
def test_soma_1():
    assert soma_1(41) == 42

#codigo de teste 2 para teste
def test_soma_1_numero_como_string():
    assert soma_1('41') == 42


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1("renata")

