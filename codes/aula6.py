conjunto = {1, 2, 3, 4, 5}
conjunto2 = {5, 6, 7, 8}

conjuniao = conjunto.union(conjunto2)
conjinter = conjunto.intersection(conjunto2)
print('Uniao: {}'.format(conjuniao))
print('Interseccao: {}'.format(conjinter))

conjdifer = conjunto.difference(conjunto2)
print('Diferenca 1 e 2: {}'.format(conjdifer))
conj2difer = conjunto2.difference(conjunto)
print('Diferenca 2 e 2: {}'.format(conj2difer))

conjdifsim = conjunto.symmetric_difference(conjunto2)
print('Diferenca simetrica 1 e 2: {}'.format(conjdifsim
                                             ))
conjunto_a = {1, 2, 3}
conjunto_b = {1, 2, 3, 4, 5}
conjsub = conjunto_a.issubset(conjunto_b)
print('Conjunto A é um subset de B: {}'.format(conjsub))
conjsup = conjunto_a.issuperset(conjunto_b)
print('Conjunto A é um superset de B: {}'.format(conjsup))

lista = ['cachorro','cachorro','gato','gato','elefante']
print('Lista animais: {}'.format(lista))
conjanimais = set(lista)
print('Conjunto animais: {}'.format(conjanimais))
lista_animais = list(conjanimais)
print('Lista animais depois: {}'.format(lista_animais))

# conjunto ={1, 2, 3, 4, 4, 4}
# conjunto.add(5)
# conjunto.discard(2)
# print(conjunto,type(conjunto))