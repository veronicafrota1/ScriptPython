# Exercicio 05
# Receber um numero e informar qual é o numero antecessor e sucessor

num = int(input('Digite um numero: '))		# recebe um valor
numAntecessor = num - 1						# calcula o antecessor
numSucessor   = num + 1						# calcula o sucessor
print('O número informado foi {}, seu antecessor é {} e o sucessor é {}'.format(num, numAntecessor, numSucessor))
