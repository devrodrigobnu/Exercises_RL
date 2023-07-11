# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# Ler valor em metros
valor_metro = float(input('Digite um valor a ser convertido: '))

# Converter em centímetors e mílimetros
cent = valor_metro * 100
mili = valor_metro * 1000

# Printar resultados
print('O valor convertido para centimentros é:', cent)
print('O valor convertido para milímetros é:', mili)
