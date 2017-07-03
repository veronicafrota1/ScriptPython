# Exercicio 07
# Calcular a media de um aluno e informar se o aluno foi aprovado ou reprovado
# media >= 6 'Aprovado'
# media < 5 'Reprovado'


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if (media >= 6):
	print('A média entre {} e {} foi {:.2f} = Aprovado.'.format(nota1,nota2,media))
elif (media <= 5):
	print('A média entre {} e {} foi {:.2f} = Reprovado.'.format(nota1, nota2,media))
