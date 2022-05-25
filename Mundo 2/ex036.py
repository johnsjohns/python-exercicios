# Exercício Python 36: 
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
salario = float(input('Valor do salario: R$'))
anos = float(input('Numero de prestações: R$'))
mensal = casa / (anos *12)
print("O valor da casa de R${:.2f}, em {:.0f} anos,\n a prestação mensal sera de R${:.2f}".format(casa, anos, mensal))
if mensal < salario * 0.3:
    print("Emprestimo concendido!")
else:
    print("Emprestimo negado!")

