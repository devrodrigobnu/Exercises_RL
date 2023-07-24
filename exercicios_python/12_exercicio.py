# 12 - Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
    # exemplo: Digite um número: 6.127. O número 6.127 tem a parte inteira 6.

# Importar a função trunc (para quebrar o numero)  
from math import trunc

# Variável e print do resultado 
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))