# lambda eh eficiente para funcoes que puderem ser resolvidas com uma unica linha
contador_letras \
    = lambda lista: [len(x) for x in lista]

lista_animais = ['cachorro', 'gato', 'elefante']
print(contador_letras(lista_animais))

soma = lambda a, b: a + b
print(soma(5, 10))
subtracao = lambda a, b: a - b
print(subtracao(10, 5))

calculadora = {
    'soma': lambda a, b: a + b,
    'subtracao': lambda a, b: a - b,
    'multiplicacao': lambda a, b: a * b,
    'divisao': lambda a, b: a / b,
}

print(type(calculadora))
soma = calculadora['soma']
multiplique = calculadora['multiplicacao']

print('A soma é: {}'.format(soma(5, 10)))
print('A multiplicacao é: {}'.format(multiplique(2, 4)))
