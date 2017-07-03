# Exercicio 06
# Receber um número, calcular o dobro, o triplo e a raiz qudrada do mesmo

num = int(input('Informe um número: '))			# recebe um valor
numDobro  = num * 2			# calcula o dobro
numTriplo = num * 3			# calcula o triplo
numRaiz   = num ** (1/2)	# calcula a raiz quadrada

# exibe mensagem
print('O dobro de {} vale {}.'.format(num, numDobro))
print('O triplo de {} vale {}.'.format(num,numTriplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(num, numRaiz))