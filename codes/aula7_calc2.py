class Calculadora:

    def soma(self, valor_a, valor_b):
        return valor_a + valor_b

    def subtracao(self, valor_a, valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
        return valor_a * valor_b

    def divisao(self, valor_a, valor_b):
        return valor_a / valor_b

calc = Calculadora()
# print('valor a = {}'.format(calc.valor_a))
# print('valor b = {}'.format(calc.valor_b))
print(calc.soma(10, 2))
print(calc.subtracao(4, 2))
print(calc.multiplicacao(100, 2))
print(calc.divisao(10, 5))