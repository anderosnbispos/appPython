class Error(Exception):
    # o pass ele passa pra frente o código
    # usado quando quero deixar vazio
    pass

class InputError(Error):
    def __init__(self, message):
        self.message = message

while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        if x > 10 or x < 0:
            raise InputError('Nota deve ser entre 0 e 10')
        # se o numero for entre 0 e 10 sai do while
        break
    except ValueError:
        print('Valor inválido. Devem ser digitados apenas números.')
    except InputError as ex:
        print(ex)


