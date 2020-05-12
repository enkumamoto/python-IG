# Funções servem para guardar um bloco de código e depois usa-los em qualquer parte do programa.
# Em caso de de precisar usar um bloco de código várias vezes num programa, a função é um meio de economizar tempo
# durante o desenvolvimento de um programa. A função é apresentada como 'def nome_da_função ()'. Dentro dos parenteses
# pode ou não conter argumentos.

# Aqui apresenta-se uma função mensagem sem argumentos.
def mensagem ():
    print ('Seja bem-vindo!')
mensagem()

# Aqui apresenta-se uma função mensagem com argumentos. Normalemnte é feito para o programa ser mais amigável com o
# usuário. Então o argumento é a variável que é usada somente dentro da função, no caso colocou-se uma variável 'user'
# para receber o nome do usuário, na função coloca-se um argumento que é uma variável 'user' ou qualquer outra
# variável (parecido como no 'loop for'). no caso abaixo usou-se uma variável diferente dentro da função (mesmo não
# tendo problema usar o 'user' (já que irá rodar dentro deste caso). No 'print' foi concatenado '+ nome' a mensagem
# de boas vindas. A variável nome não tem valor atribuido, porém a variável terá valor quando a função for chamada
# pelo programa. Concatena-se a variável nome que receberá o valor vindo da variável user.
# OBS: Se uma função for criada com argumento, ela não poderá ser chamada sem argumento.
user = 'eiji'
def mensagem (nome):
    print ('Seja bem-vindo, ' + nome.title() + '!') #Adcionado um '.title()' para que a primeira letra do nome fique em maiúculo.
mensagem(user)

# Um programa pode conter diversas mensagens diferentes para diferentes coisas, a melhor prática é criar um arquivo com
# as mensagens necessárias e suas devidas funções.
# outra coisa que também pode ser feita é uma função com vários argumentos, isso pode ser feito separando os arqumentos
# por vírgula. Por exemplo, uma função para calcular o IMC ( Índice de Massa Corpórea).
#name = input ('Digite seu nome: ')
#peso = float(input('Digite seu peso: '))
#altura = float(input('Digite sua altura (Ex. 1.78): '))
def imc (peso,altura):
    valor_imc = peso / (altura*altura)
# Quando usado o comando 'return' o resutado dessa função se tornará este resultado e se tornando resultado pode-se usar
# a função como uma variável.
    return (valor_imc)
# Abaixo colocou-se decisões para a função e assim já pode-se usar a função para calculo ou comaprações.
if imc (86,1.84) > 32:
    print ('Obesidade.')
else:
    print ('Ainda não está obeso.')

#print (name, 'seu IMC é:' + valor_imc)

# As funções podem ser usadas dentro dos 'loops', condicionais, função dentro de função e vice-versa.
# Dentro do IDLE uma vez usada a função seus valores são perdidos. Usando o código abaixo no IDLE, a função rodará
# normalmente mas perderá todos os resultados quando finalizar, mesmo contendo uma variável nela, pois a variável so
# foi usada no momento específico do exemplo.
def exemplo ():
    y = 10
    print (y)
exemplo()