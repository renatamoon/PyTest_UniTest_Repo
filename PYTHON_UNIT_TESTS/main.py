from calculadora import soma


try:
    print(soma('10', 20))
except AssertionError as e:
    print('CONTA INVÁLIDA: {e}')