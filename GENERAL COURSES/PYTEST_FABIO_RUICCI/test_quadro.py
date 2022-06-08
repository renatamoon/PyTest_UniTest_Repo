# fixture é uma forma de evitar repetição de codigo em testes

def test_have_no_exist_none_column_on_the_board():
    quadro = Quadro()  # data
    quantidade_de_coluna = len(quadro.colunas)
    assert len(quadro.colunas) == 0
