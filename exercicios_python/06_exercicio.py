
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere USD 1.00 = R$ 5.00

# Ler quanto dinheiro a pessoa tem na carteira
carteira = int(input('Digite quanto você tem em carteira - R$: ', ))

# Variável para calcular dólar
dolar = carteira * 5

# Printar resultado

print('Você pode obter', dolar, 'USD')
