from math import sin, cos, tan, radians
angulo = float(input('Digite o angulo que você deseja:' ))
print('o angulo de {} tem o seno de {:.2f}'.format(angulo, sin(radians(angulo))))
print('o angulo de {} tem o cosseno de {:.2f}'.format(angulo, cos(radians(angulo))))
print('o angulo de {} tem a tangente de {:.2f}'.format(angulo,tan(radians(angulo))))