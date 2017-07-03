# Exercicio 4 - VSF
# Programa que le algo e exibe seus tipos primitivos e todas as informações sobre ele

a = input('Digite algo: ')	# Recebe uma informação

print('O tipo primitivo desse valor é', type(a))	# informa o tipo 
print('Só tem espaços ? ', a.isspace())				# informa se existe somente espaços
print('É um número? ', a.isnumeric())				# Informa se o que foi digitado é um numero
print('É alfabético? ', a.isalpha())				# Informa se  o que foi digitado é alfabéticp
print('É alfanumerico? ', a.isalnum())				# Informa se  o que foi digitado é alfanumerico
print('Está em maiusculo? ', a.isupper())			# Informa se  o que foi digitado esta em maiusculo
print('Está em minusculo? ', a.islower())			# Informa se  o que foi digitado esta em minusculo
print('Eatá captalizada? ', a.istitle())			# Informa se  o que foi digitado esta captalizado
