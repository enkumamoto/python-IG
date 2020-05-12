# O 'for' trabalha do mesma forma como o 'while', ou seja, com repetição. O funcionamento do 'for' é por sequência,
# como 'strings' são sequências de caractéres, 'listas e tuplas' são sequências ordenadas de elementos e os
# ´dicionários' são sequências de pares que são composto por uma chave e um valor.
# Por exemplo, com o 'loop for' pode-se percorrer toda a lista e analisar separadamente cada um dos elementos.
# Pode-se colocar qualquer variável, se vê muito usar a letra 'i' como variável para trabalhar com 'for". Esta estrutura
# mostrará que a cada passagem neste 'loop' será pego um elemento da lista e dirá que o 'i' é o elemento e fará isso com
# todos até o final da lista
#compras = ['arroz', 'feijão','macarrão','carne']
#for i in compras:
#    print (i)

# Por exemplo a 'string' abaixo apresenta o nome joaquim, onde cada letra do nome é um índice. Quando executar
# o programa será apresentada cada petra do nome separadamente.
#nome = 'joaquim'
#for i in nome:
#    print (i)

# O 'loop for' também pode ser usado para realizar operações matemáticas. Por exemplo, um funcionário de uma loja
# que realizar varias vendas e ele precisa sabe o somatório das vendas.
#vendas = [1000,450,300,920,600]
#total = 0
#for i in vendas:
#    total += i
#print ('Você vendeu um total de:',total,'reais')

# O 'loop for' também pode ser usado com dicionários, abaixo o expmplo mostra que o 'for' irá listar as chaves do
# dicionário.
#cores = {'vermelho':'red', 'azul': 'blue', 'verde':'green', 'preto': 'black', 'laranja':'orange'}
#for i in cores:
    #print (i)
# Para o 'for' ter acesso aos valores da chavee deve-se usar na linha a variável cores e entre colchetes o 'i'. Ao
# executar o programa será apresentado os valores das chaves.
    #print (cores[i])
# Para o 'for' apresentar a chave e o valor a linha deve ser escrita da seguinte forma:
# Lembrando que dentro deste printe pode-se colocar alguma 'string' para que organize o que vai ser impresso
#    print (i,'em inglês é',cores[i])

# Existe o 'for loop' aninhado é feito, por exemplo, com listas dentro de outras listas (ou laços dentros de laços)
# No caso abaixo mostra-se que o 'loop' passará pela primeira lista, depois pela segunda e depois pela terceira. Caso
# tenha mais laços o 'loop' permanecerá até passar pela última lista.
#compras = [['arroz', 'feijão','macarrão'],['carne', 'frango','peixe'],['leite','iogurte']]
#for i in compras:      # Esta linha seguida de 'print' irá mostrar as listas separadamente.
#    print (i)          # Com este "print' descomentado o programa irá mostrar cada lista separadamente e seus itens
#    for item in i:     # Com a adição desta linha será apresentada cada item das listas separadamente.
#        print (item)

# Caso queira realizar repetiçoes limitadas pode-se usar o 'range'. Sabe-se que com o 'while' pode-se usar uma variável
# 'x > 10' fazer o comando que quer e a cada passagem o x tem uma unidade aumentada por passagem. Mas no 'loop for'
# pode-se fazer da seguinte forma abaixo. O resultado será a apresentacão dos número de 0 a 9 (para a computação o 0
# éo primeiro número). Se quer imprimir realmente de 0 - 10 pode-se fazer de duas formas: A primeira, no 'range' deve
# ser colocado de 0 - 11 ou colocar print (i+1). Também pode fazer uma contagem regressiva, basta colocar 'print (10-i)'
for i in range (0,10):
    print (i)