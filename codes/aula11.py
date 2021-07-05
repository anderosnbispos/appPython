# Como lancar uma exceção genérica
# Utilizar exceções específicas
# Encadeamento de exceções
# Else e Finally
# Criação de exceções customizadas

lista = [1, 10]
arquivo = open('teste.txt','r')
try:
    texto = arquivo.read()
    divisao = 10 / 1
    numero = lista[1]
except ZeroDivisionError:
    print('Erro de divisão por 0')
except IndexError:
    print('Erro ao acessar indice inexistente')
except Exception as ex:
    print('erro desconhecido. Erro: {}'.format(ex))
else:
    print('executa quando nao ocorre excessao')
finally:
    print('sempre executa')
    print('fechando arquivo')
    arquivo.close()
# except:
#     print('Erro desconhecido')