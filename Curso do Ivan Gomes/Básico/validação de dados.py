# Para realizar validação de dados usaremos o programa fatura.
# A variável 'valor' recebe 'float', isso faz com que o python receba valores com casa decimais usando '.' mas no Brasil
# as casas decimais separa-se com vírgula. Neste caso será convertido os valores de vírgula para ponto.

print ('Bem vindo ao DigVend')

repeat = 's'
fatura = []
total = 0
valid_valor = False

while True:
    produto = input ('Digite o nome do produto que quer comprar: ')

# Foi retirado o 'float' da linha abaixo porque se digitado uma palavra ou valor com virgula o python apresentará um
# erro de 'string' e adicionado um 'while' com uma variável 'valid_valor' (e também no início do# programa). Desta forma
# o programa so sairá do 'loop' se conseguir validar o valor. A idéia é converter de 'string' para 'float'.
    while valid_valor == False:
        valor = (input('Digite o preço do produto: '))                                                                  #No programa original o pedido do preço no primeiro 'loop'
        try:                                                                                                            #O comando 'try' tenta realizar a tarefa, caso não consiga o comando parte para uma excessão (except).
            valor = float(valor)
            if valor <= 0:                                                                                              #Aqui o programa evita que o valor do produro seja menor que zero (valores negativos)
                print ('O preço precisa ser maior que zero!')
            else:                                                                                                       #O 'else' fará o 'loop' caso o valide o valor do produto.
                valid_valor = True                                                                                      #Esta linha confirma o 'try', ou seja, se a conversão de 'string' para 'float'
                                                                                                                        #ocorrer, então o programa sairá do 'loop'. Se não, ele irá para o 'except'.
        except:
            print ("formato de preço inválido. Use apenas números e separe os centavos com '.'.")
    fatura.append ([produto,valor])                                                                                     #Aqui acrescentará o produto e preço a lista fatura.
    total += valor                                                                                                      #Aqui adiciona o valor do produto ao total para ser somado
    valid_valor = False                                                                                                 #Esta variável volta a ser falsa para que o 'loop' não ser infinito, pois acima declarou-se que
                                                                                                                        #a variável era verdadeira.
    repeat = input ('Deseja comprar outro produto? S ou N: ').lower()                                                   #Aqui questiona o usuário se quer ou não mais produtos.
    if repeat == 's':
        continue                                                                                                        #Condições para decisão do programa para continuar ou finalizar.
    elif repeat =='n':
        break

for i in fatura:                                                                                                        #Quando o break é acionado, fará o loop da fatura ser apresentada separadamente.
    print (i[0],'- R$',i[1])

print ('O total da fatura é: R$',total)