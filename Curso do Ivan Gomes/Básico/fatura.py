print ('Bem vindo ao DigVend')

repeat = 's'
fatura = []
total = 0

while True:
    produto = input ('Digite o nome do produto que quer comprar: ')
    valor = float (input ('Digite o preço do produto: '))
    fatura.append ([produto,valor]) #Aqui acrescentará o produto e preço a lista fatura.
    total += valor #Aqui adiciona o valor do produto ao total para ser somado
    repeat = input ('Deseja comprar outro produto? S ou N: ').lower() #Aqui questiona o usuário se quer ou não mais produtos
    if repeat == 's':       #
        continue            #Condições para decisão do programa para continuar ou finalizar.
    elif repeat =='n':      #
        break               #

for i in fatura:            #Quando o break é acionado, fará o loop da fatura ser apresentada separadamente.
    print (i[0],'- R$',i[1])

print ('O total da fatura é: R$',total)