dias = float(input('Quantos dias o carro foi alugado: '))
rodado = float(input('Quantos Kilometros foram rodados: '))
print('O total a pagar é de R${:.2f}'.format((dias * 60) + (rodado * 0.15)))