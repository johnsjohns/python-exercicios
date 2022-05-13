velocidade = float(input('Qual é a velociade do carro? '))
if velocidade > 80:
    print('Você excedeu o limite de velocidade de 80 KM')
    multa = (velocidade - 80) * 7
    print('Você deve pagar R${} de multa'.format(multa))
print('Tenha um bom dia e dirija com cuidado')