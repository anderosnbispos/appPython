##!/usr/local/bin/python3.9
a = int(input('Entre com o primeiro valor (a): '))
b = int(input('Entre com o segundo valor (b): '))

soma = a + b
subtrai = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print('a = {} / b = {}'.format(a, b))
print('Soma: {soma}.'
      '\nSubtracao: {sub}.'
      '\nMultiplicacao: {multi}'
      '\nDivisao {div}'
      '\nResto {resto}'
      .format(soma=soma,
              sub=subtrai,
              multi=multiplicacao,
              div=divisao,
              resto=resto))

#print('soma: ' + str(soma))
# print('subtracao: ' + str(subtrai))
# print(multiplicacao)
# print(int(divisao))
# print(resto)

# x = '1'
# soma2 = int(x) + 1
# print(soma2)