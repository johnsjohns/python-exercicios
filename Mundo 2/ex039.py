# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano = date.today().year -ano
if ano < 18:
    print('Você ainda vai se alistar em {} anos'.format(18 - ano))
elif ano == 18:
    print('Já é hora de você se alistar')
else:
    print('Você esta atraso em {} anos para o alistamento'.format(ano - 18))
