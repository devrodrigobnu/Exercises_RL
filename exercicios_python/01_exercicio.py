# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor


# Ler o número do usuário
numero = int(input('Digite um número inteiro: '))

# Variáveis para definir o sucessor e o antecessor
antecessor = numero - 1
sucessor = numero + 1

# Print para mostrar ao usuário o resultado.
print('O antecessor de', numero, 'é', antecessor)
print('O sucessor de', numero, 'é', sucessor)