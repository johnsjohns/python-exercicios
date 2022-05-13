km = float(input('Digite a distâcia em KM: '))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print('O custo da passagem é de R${}'.format(valor))