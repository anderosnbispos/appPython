class Calculadora:

    def __init__(self, num1, num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_b + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

    def multiplicacao(self):
        return self.valor_a * self.valor_b

    def divisao(self):
        return self.valor_a / self.valor_b

if __name__ == '__main__':
    calc = Calculadora(10, 2)
    print('valor a = {}'.format(calc.valor_a))
    print('valor b = {}'.format(calc.valor_b))
    print(calc.soma())
    print(calc.subtracao())
    print(calc.multiplicacao())
    print(calc.divisao())


# def soma(a, b):
#     return a + b
#
# def subtracao(a, b):
#     return a - b
#
# def multiplicacao(a, b):
#     return a * b
#
# def divisao(a, b):
#     return a / b
#
#
# print(soma(1, 2))
# print(soma(2, 4))
# print(subtracao(4, 2))

