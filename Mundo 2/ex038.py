#Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem:
#– O primeiro valor é maior
#– O segundo valor é maior
#_Não existe valor maior, os dois são iguais

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite o segundo numero: '))
if n1 > n2:
    print('O primeiro valor é o maior')
elif n2 > n1:
    print ('O segundo valor é p maior '.format(n2, n1))
else:
    print(' Não exite valor maior, os dois são iguais')