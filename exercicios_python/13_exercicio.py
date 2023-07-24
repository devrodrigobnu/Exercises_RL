# 13 - Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa

# Variáveis
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

# Condição e print
hipo = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hipo))