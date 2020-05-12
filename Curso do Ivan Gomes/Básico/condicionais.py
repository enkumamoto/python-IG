# As condicionais é dar a capacidade de decisão ao programa. As condicionais são 'if', 'else' e 'elif'. Essas
# condicionais trabalham em cima de Verdadeiro (True) ou Falso (False). No exemplo abaixo a idade é igual a 17, mas
# a condicional é que: se for maior ou igual a 18, deve-se retornar a mensagem teste. Como 17 não é maior ou igual a 18
# o programa não retorna erro ou mensagem.
idade = 17
if idade >= 18:
    print ('teste')

# Já no caso abaixo a idade é igual a 18, logo retornará a mensagem 'teste'.
idade = 18
if idade >= 18:
    print('teste')

# Também pode-se usar o símbolo de menor para realizar as comparações dentro do programa. Caso a variável tenha que ter
# o valor exatamente igual ao que se procura, deve-se usar '=='. Um igual só é atribuição de valor a variável.
idade = int(input('Digite sua idade: '))
if idade == 18:
# Aqui vemos uma indetação, pois está na mesma linha que a primeira decisão ou dentro do 'if'.
    print('A idade é igual a 18!')
#   print ('dentro do if')

# Uma das coisas que podem ser acrescentadas entre um 'if' e um 'else' é um 'elif'. É como se fosse para ter uma nova
# condição antes da decisão final do programa. O 'elif' significa 'senão se'.
elif idade == 17:
    print ('A idade é igual a 17!')

# Já aqui está fora da indentação ou fora do 'if' e por isso ele imprime a linha abaixo de qualquer maneira
#print ('fora do if')
# O 'if' pode trabalhar sozinho na qu17estão acima, porém caso seja declarada uma idade diferente o programa tem que tomar
# uma decisão, então será usado um 'else'. O 'else' deve vir em seguida (na mesma linha) do 'if'
else:
    print ('A idade não é 17 e nem 18!')

# Uma outra forma de verificar o valor de algo é diferente dentro dos operadores é usando '!=' que significa
# "não é igual a...". Com esse operador o if continua procurando algo que seja exatamente igual ao valor atribuído.
# Se digitar no IDLE: idade = 17 e depois digitar idade != 18 o IDLE do python retornará True, por que está realmente
# afirmando que 17 é diferente de 18.
idade = int(input('Digite sua idade: '))
if idade != 18:
    print ('A idade não é igual a 18!')

# No python qualquer valor tem atrelado a ele Verdadeiro ou Falso, por exemplo:
y = 5
if y:
    print ('teste')

# Lembre-se que o python considera qualquer valor vazio ou 0 igual a falso. Abaixo pode ver que o y = 0 o que
# vai acontecer é que a linha de print não será executada por que ela é falsa. Se o valor for diferente de zero
# o python considera verdadeiro. Segue exemplo:
y = 0
if y:
    print ('teste')

# Pode-se terstar se alguma lista ou dicionário tem valor ou não, por exemplo se abre uma lista mas não se coloca
# valores:
lista1 = []
if lista1:
    print ('Lista tem valores')

# OBS: No IDLE pode usar o 'else' porque só pode executar um comando por vez.
# Se colocar algum valor na lista ou no Dic. o comando acima imprimirá a mensagem. Segue exemplo:
lista1.append ('joao')
print (lista1)
if lista1:
    print ('Lista tem valores')
