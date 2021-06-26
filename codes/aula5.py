nota = list()
for x in range(0, 4):
    notatemp = int(input('Entre a nota do bimestre {}:'
                        .format(x+1)))
    while notatemp > 10:
        notatemp = int(input('Você digitou um número errado.'
                             'Entre a nota do bimestre {}:'.format(x+1)))

    nota.append(notatemp)

print('As notas foram: {}'.format(nota))
media = sum(nota)/4
print('A média do aluno foi: {}'.format(media))

#     while nota[x] > 10:
#         nota[x] = int(input('Você digitou um número errado.'
#                             'Entre a nota do bimestre {}:'.format(x)))
#
# media = sum(nota) / 4
#
# print('A média do aluno é {}'.format(media))

# lista = [1, 10, 7, 3]
# animal = ['cachorro','gato','elefante','lobo','arara']
#
# tupla = (1, 10, 12, 14)
#
# tanimal = tuple(animal)
# print(animal,type(animal))
# print(tanimal,type(tanimal))
#
# ltupla = list(tupla)
# print(tupla,type(tupla))
# print(ltupla,type(ltupla))


# animal[0] = 'macaco'
# print(animal)
# print(len(animal))
#
#
# print(tupla[2])
# print(len(tupla))

# lista.sort()
# animal.sort()
# print(lista)
# print(animal)
#
# lista.reverse()
# animal.reverse()
# print(lista)
# print(animal)

# newanimal = animal * 3
# print(newanimal)

# if 'veado' in animal:
#     print('sim')
# else:
#     print('nao')
#     animal.append('veado')
#     print(animal)
#
# animal.pop()
# print(animal)

# print(sum(lista))
# print(min(lista))
# print(max(lista))
#
# print(max(animal))
# print(lista,type(lista))
# print(animal,type(lista))

# soma = 0
# for x in lista:
#     print(x)
#     soma += x



# for x in animal:
#     print(x)