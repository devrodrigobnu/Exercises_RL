# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada

# Ler número do usuário
numero = int(input('Digite um número: '))

# Usar while para percorrer os numeros de 1 a 10
i = 1

# Configurar o loop, multiplicar o numero lido pelo alor atual do loop 
# Printar o resultado do loop
while i <= 10:
    resultado = numero * i
    print(numero, 'x', i, '=', resultado)
    i += 1



