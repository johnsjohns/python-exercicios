altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
print('Sua parede tem a dimensao de {}x{} e sua area é de {}m²'.format(altura, largura, area))
print(' Para pintar sua parade você precisará de {}l de tinta'.format(area/2))  