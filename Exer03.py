# Exercicio 06
# Receber um número, calcular o dobro, o triplo e a raiz qudrada do mesmo

num = int(input('Informe um número: '))
numDobro  = num * 2
numTriplo = num * 3
numRaiz   = num ** (1/2)

print('O dobro de {} vale {}.'.format(num, numDobro))
print('O triplo de {} vale {}.'.format(num,numTriplo))
print('A raiz quadrada de {} vale {:.2f}.'.format(num, numRaiz))