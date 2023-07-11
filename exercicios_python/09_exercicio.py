# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Ler salário de um funcionário
salario = float(input('Digite seu salário:R$ '))

# Calcular aumento do salário
aumento = salario * 0.15
salario_novo = salario + aumento

# Printar o resultado

print('O seu salário de R$', salario, 'teve um reajuste e o novo salário a partir de hoje será de R$', salario_novo)
