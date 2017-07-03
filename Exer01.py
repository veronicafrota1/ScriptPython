# Exercicio 4 - VSF
# Programa que le algo e exibe seus tipos primitivos e todas as informações sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços ? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiusculo? ', a.isupper())
print('Está em minusculo? ', a.islower())
print('Eatá captalizada? ', a.istitle())
