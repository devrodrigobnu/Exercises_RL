# Dicionário com os produtos e seus respectivos preços
produtos = {
    '1': 10.00,
    '2': 15.00,
    '3': 17.00,
    '4': 4.00
}


# Solicitar ao usuário o código do produto e o valor pago
codigo_produto = input("Digite o codigo do produto: ")
valor_pago = float(input("O valor pago foi: "))


# Verificar se o código do produto existe
if codigo_produto in produtos:
    preco_produto = produtos[codigo_produto]


# Verificar se o valor pago é suficiente
if valor_pago >= preco_produto:
    troco = preco_produto - valor_pago
    print("Troco: R$", troco)
else:
    print("Valor pago insuficiente!")

