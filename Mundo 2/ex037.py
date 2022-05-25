# Exercício Python 37: 
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário,# 2 para octal e 3 para hexadecimal.

numero = int(input('Digite o numero: '))
print('[1] Converter para binário')
print('[2] Converter para octal')
print('[3] Converter para hexadecimal')
opcao = int(input('Escolha uma opção: '))
if opcao == 1:
    print('{} em binario é {}'.format(numero, bin(numero)[2:]))
elif opcao == 2:
    print('{} em octal é {}'.format(numero, hex(numero)[2:]))
elif opcao == 3:
    print('{} em hexadecimal é {}'.format(numero, oct(numero)[2:]))
else:
    print('Opção invalida')