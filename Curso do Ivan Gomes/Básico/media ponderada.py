# Exercício: Faça um programa para calcular a média ponderada de um aluno. Para isso, peça ao
# usuário os pesos das duas provas e as notas do aluno. Ao final, imprima a média ponderada do aluno.

print ('Calcule sua média e saiba se passou de ano!')

peso1 = float(input('Digite o peso da primeira prova: '))
peso2 = float(input('Digite o peso da segunda prova: '))

nota1 = float(input ('Digite a nota da sua primeira prova: '))
nota2 = float(input ('Digite a nota da sua segunda prova: '))

media = ((nota1*peso1)+(nota2*peso2))/(peso1+peso2)

#$print ('Sua média é: ',media)

if media >= 7.0:
    print ('Parabéns, você passou com média: ',media)
else:
    print ('Você fará recuperação, sua média é: ',media)

input ('Aperte Enter para sair.')