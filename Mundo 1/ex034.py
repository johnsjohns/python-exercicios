salario = float(input('Digite o valor do salario salário: R$'))
if salario > 1250:
    salario = salario + (salario * 0.1);
else:
    salario = salario + (salario * 0.15)
print('Novo salário: R${:.2f}'.format(salario))