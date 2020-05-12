# Programa para calcular as médias dos alunos somando as duas notas com desconto em cima do percentual de faltas.
# Considere que foram dadas 20 aulas e que para passar o aluno precisa de pelo menos 70% de presença e a média 6,0
# ou mais. Ao final imprima:
# Nome do aluno
# Média
# Percentual de Presença (assiduidade)
# Resultado ( Reprovado por faltas e por média. Reprovado por faltas, Reprovado por média, Aprovado)

nome = input('Digite seu nome Completo: ')
nota1 = float(input('Digite a nota da primeira prova: '))
nota2 = float(input('Digite a nota da segunda prova: '))
faltas = int(input('Digita a quantidade de faltas: '))                                                                  # Curso com 20 aulas, exige 70% de presença, ou seja, 14 aulas. Aluno com 6 faltas está reprovado.
media = ((nota1 + nota2)/2)
percentual = ((20 - faltas) / 20 * 100)

if media >= 6 and percentual >= 70:
    resultado = 'aprovado!'

elif media < 6 and percentual < 70:
    resultado = 'reprovado por média e por faltas.'

elif media < 6:
    resultado = 'reprovado por média.'

elif percentual < 70:
    resultado = 'reprovado por faltas.'

else:
    print ('Erro.')

print ('Olá',nome,', informamos que sua média é',media, 'e sua assiduidade foi de',percentual,'%. Com isso você foi',resultado)