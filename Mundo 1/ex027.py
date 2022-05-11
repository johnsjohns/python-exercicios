nome = input('Digite seu nome completo: ')
divido = nome.split(' ')
print('Seu primeiro nome é: {}'.format(divido[0]))
print('Seu ulrimo nome é: {}'.format(divido[len(divido) - 1]))