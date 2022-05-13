from random import randint
from time import sleep
print('-=-'*33)
print('Vou pensar em um número de 0 5. Tente adivinhar...')
meuNumero = randint(0,5)
print('-=-'*33)
numero = int(input('Em qual numero eu pensei? '))
print('\033[92m Processando...\033[90m')
sleep(2)
if numero == meuNumero:
    print('Parabens, você adivinhou o numero {}'.format(meuNumero))
else:
    print('Vocẽ errou, eu pensei no numero {} e não no numero {}'.format(meuNumero, numero))