from random import shuffle
a1 = input('Primeiro Aluno: ')
a2 = input('Segundo Aluno: ')
a3 = input('Terceiro Aluno: ')
a4 = input('Quarto Aluno:  ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('O aluno sorteado foi: {}'.format(lista))