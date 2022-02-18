import pytest


def soma_1(numero):
    return int(numero) + 1


# esse teste é falho
def test_soma_1():
    assert soma_1(41) == 42


# esse teste é falho
def test_soma_1_numero_como_string():
    assert soma_1("41") == 42


def test_soma_1_palavra():
    with pytest.raises(ValueError):
        soma_1("fabio")
