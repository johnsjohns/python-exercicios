a = int(input('Primeiro numero: '))
b = int(input('Seguno numero: '))
c = int(input('Terceiro numero: '))

menor = a
if b <a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c 

print('O menor valor digitado foi {}'.format(menor))
print('o maior valor digitado foi {}'.format(maior))