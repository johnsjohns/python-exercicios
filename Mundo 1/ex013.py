salario = float(input('Qual é o salário do funcionario: R$'))
print('Um funcionário que ganha R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, salario + (salario * 15 / 100)))