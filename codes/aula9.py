# aula 9 - DIO - Introducao a programacao Python
# by Rafael Galleani
# Ementa:
# trabalhando com arquivos:
# - gerar e escrever em um arquivo
# - ler informacoes de um arquivo
# - trabalhar com informacoes dos arquivos
# - trabalhar melhor com strings
# - mais um pouco de lambda
# - copiar e mover arquivos

# parametros de escrita:
# w = cria e escreve ou sobreescreve
# a = cria e atualiza
# r = ler arquivo
#file = open('teste.txt','w') - anterior

# modulo de manipulacao de arquivos - usado para copiar e mover
import shutil

def escrever_file(texto):
    dir = '/Users/Anderson/Documents/workspace/appPython/teste.txt'
    file = open(dir,'w')
    file.write(texto)
    file.close()

def atualizar_file(nome_arquivo, texto):
    file = open(nome_arquivo,'a')
    file.write(texto)
    file.close()

def ler_file(nome_arquivo):
    file = open(nome_arquivo,'r')
    texto = file.read()
    print(texto)

def media_notas(nome_arquivo):
    file = open(nome_arquivo, 'r')
    aluno_nota = file.read()
    # print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    # print(aluno_nota)
    lista_media = []
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        media = lambda notas: sum([int(i) for i in notas])/4
        lista_media.append({aluno:media(lista_notas)})
    return lista_media

def copia_arquivo(nome_arquivo):
    shutil.copy(nome_arquivo,'/Users/Anderson/Documents/workspace/notas_bkp.txt')

def move_arquivo(nome_arquivo):
    shutil.move(nome_arquivo,'/Users/Anderson/Documents/workspace/notas_bkp.txt')

if __name__ == '__main__':

    # Teste de movimentacao dos arquivos
    move_arquivo('notas.txt')

    # Teste de copia dos arquivos
    # copia_arquivo('notas.txt')
    # lista_media = media_notas('notas.txt')
    # print(lista_media)
    # escrever_file('Primeira Linha.\n')
    # aluno = 'Alice,10,10,10,10\n'
    # atualizar_file('notas.txt',aluno)
    # ler_file('teste.txt')