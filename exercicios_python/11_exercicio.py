# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0.15 por Km rodado.

# Ler dados
dias = int(input('Digite quantos dias o carro foi alugado: '))
km = float(input('Digite quantos km foram rodados: '))

# Converter dados
preco_pagar = (60 * dias) + (km * 0.15)

# Printar dados
print('O total a pagar é de R$',preco_pagar)