# Programa para calcular as médias dos alunos somando as duas notas com desconto em cima do percentual de faltas.
# Considere que foram dadas 20 aulas e que para passar o aluno precisa de pelo menos 70% de presença e a média 6,0
# ou mais. Ao final imprima:
# Nome do aluno
# Média
# Percentual de Presença (assiduidade)
# Resultado ( Reprovado por faltas e por média. Reprovado por faltas, Reprovado por média, Aprovado)
# Neste programa temos a validação das notas e faltas e o programa não pode fechar por erro.

nome = input('Digite seu nome Completo: ')

valid_nota = False
while valid_nota == False:
    nota1 = input('Digite a nota da primeira prova: ')
    try:
        nota1 = float(nota1)
        if nota1 < 0 or nota1 > 10:
            print ('Nota inválida. Valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print ('Nota inválido. Use apenas números e separe oos decimais com ponto. (Ex. 9.5)')
valid_nota = False

while valid_nota == False:
    nota2 = input('Digite a nota da segunda prova: ')
    try:
        nota2 = float(nota2)
        if nota2 < 0 or nota2 > 10:
            print ('Nota inválida. Valor deve ser entre 0 e 10')
        else:
            valid_nota = True
    except:
        print ('Nota inválido. Use apenas números e separe oos decimais com ponto. (Ex. 9.5)')
valid_faltas = False

while valid_faltas == False:
    faltas = input('Digita o total de faltas: ') # Curso com 20 aulas, exige 70% de presença, ou seja, 14 aulas. Aluno com 6 faltas está reprovado.
    try:
        faltas = float(faltas)
        if faltas < 0 or faltas > 20:
            print ('Número de faltas inválido, Valor deve ser entre 0 e 20.')
        else:
            valid_faltas = True
    except:
        print('Número de faltas inválido. Use apenas números e separe oos decimais com ponto. (Ex. 15.5)')

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
