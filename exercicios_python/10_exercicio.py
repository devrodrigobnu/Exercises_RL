# Escreva um programa que converta uma temperatura digitada em Celsius e converta para fahrenheit

# Ler dados 
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))

# Converter dados
f_to_c = (fahrenheit - 32) * 5/9
c_to_f = (celsius * 9/5) + 32

# Printar resultados
print('A temperatura em celsius informada foi',celsius, 'e a sua conversão para fahrenheit é de:', c_to_f,'ºF')
print('A temperatura em fahrenheit informada foi',fahrenheit, 'e a sua conversão para celsius é de:', f_to_c,'ºC')
