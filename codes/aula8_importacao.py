from aula7_tv import Televisao
from aula7_calc1 import Calculadora
from aula8_contador_letras import contador_letras

if __name__ == '__main__':
    tv = Televisao()
    print(tv.ligada)
    tv.power()
    print(tv.ligada)

    calc = Calculadora(5, 10)
    print(calc.soma())

    animais = ['gato','cachorro']

    total_letras = contador_letras(animais)
    print('O total de letras de cada palavra da lista é '
          '{}'.format(total_letras))