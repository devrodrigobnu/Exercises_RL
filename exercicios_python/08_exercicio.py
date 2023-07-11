# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# Ler dados (preço)
preco_produto = float(input('Digite o preço do produto:R$ '))

# Desconto de 5%
desconto = 100 * 0.05
valor_final = preco_produto - desconto

# Printar o resultado
print('O valor final do produto com desconto é: ', valor_final)