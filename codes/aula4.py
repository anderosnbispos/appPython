a = int(input('Primeiro bimestre: '))
while a > 10:
        a = int(input('Você digitou um número'
                      ' errado. Primeiro bimestre: '))
b = int(input('Segundo bimestre: '))
while b > 10:
        b = int(input('Você digitou um número'
                      ' errado. Segundo bimestre: '))
c = int(input('Terceiro bimestre: '))
while c > 10:
        c = int(input('Você digitou um número'
                      ' errado. Terceiro bimestre: '))
d = int(input('Quarto bimestre: '))
while d > 10:
        d = int(input('Você digitou um número'
                      ' errado. Quarto bimestre: '))

media = (a + b + c + d) / 4

print('A média do aluno é {}'.format(media))

# a = 0
# while a <= 10:
#     print(a)
#     a += 1

# b = int(input('Entre com o número: '))
# total = 0
# for a in range(b+1):
#     div = 0
#     for x in range(1, a+1):
#         resto = a % x
#         if resto == 0:
#             div += 1
#
#     if div == 2:
#         print('número {} é primo'.format(a))
#         total += 1
#
# print('TOTAL: de 0 a {}, existem {} primos'
#       .format(b, total))

# a = int(input('Entre com o número: '))
#
# div = 0
# for x in range(1, a+1):
#     resto = a % x
#     if resto == 0:
#         div = div + 1
#
# if div == 2:
#     print('número {} é primo'.format(a))
# else:
#     print('número {} não é primo'.format(a))


# for x in range(1, 101):
#     print(x)

