# 'loop's sempre está presente em qualquer programa. O 'loop' é uma estrutura de repetição, por exemplo, nos programas
# feitos anteriormente o que acontece é todos rodam, terminam mas não voltam para o começo. Mesmo com condicionais,
# o programa realiza algumas tarefas mas assim que comcluído o programa termina. Com o 'loop' pode definir quais
# comandos podems repetir e por quanto tempo, isso permite que o programa não termine assim que finaliza suas
# tarefas ou só feche quando o usuário feche o programa. Aqui temos os dois principais 'loops', o primeiro será
# o 'while'.
# O 'while' significa enquato e na linha abaixo diz o seguinte: "equanto x for menor que 1" o comando dentro da
# indentação deve ser repetido e nunca sairá do 'loop'. Por que foi dito que "equanto x for menor que 1" e o 'x = 0',
# ou seja, é um 'loop' infinito.
# OBS: Caso esteja usando algum shell para executar um 'loop' infinito, use CTRL+c para cancelar a execução.
# OBS2: As linhas abaixo estão comentadas para não atrapalhar o exemplo seguinte a este.
#x = 0
#while x < 1:
#    nome = input ('Qual o seu nome? ')

# No exemplo abaixo, será apresentado um 'loop' finito:
# OBS3: As linhas abaixo estão comentadas para não atrapalhar o exemplo seguinte a este.
#x = 0

# Aqui informa-se que 'x' será menor que 4
#while x < 4:
#    nome = input ('Qual o seu nome? ')
# Para confirmar que o nome digitado está sendo capturado durante o loop, coloca-se um 'print' como na linha abaixo como
# teste.

#    print ('Olá',nome)
# Na linha abaixo será colocado como o programa entenderá que o 'loop' é finito. Quando diz que 'x = x +1' o 'while'
# passará por esta operação e realizará a mesma em todas as passagens e guardando esta informação a cada passagem,
# ou seja, o 'x' deixará de ser 0 e passará a ser somado mais 1 e a informação será guardada no 'x'. Com isso, quando
# o valor atingir o valor de x dentro do 'while'.
#    x = x + 1 # Ou pode usar o operador 'x +=1'. Este operador significa 'x' é igual a ele mesmo mais 1 (ou a quantidade
              # que deve ser somado ou subtraido ou qualquer outra operação matemática que deseja realizar).

# OBS4: As linhas abaixo estão comentadas para não atrapalhar o exemplo seguinte a este.
# No exemplo abaixo veremos um 'loop' incluindo itens a uma lista.
#x = 0

# Para criar uma lista deve-se abrir uma lista vazia após a variável inicial do 'loop'.
#pessoas = []
#while x < 4:
#    nome = input ('Qual o seu nome? ')

# Para incluir os nomes das pessoas na lista deve-se usar o 'lista.append' seguido da variável desejada, neste caso nome.
#    pessoas.append (nome)
#    x += 1
# Para confirmar que a lista está sendo preenchida será impressa as informações a cada 'loop'. Mas caso queira que o
# programa só apresente a lista depois de capturar todos os nomes, basta tirar o 'print' da indentação e colocar na
# mesma linha que o 'while'.
    #print (pessoas)
#print (pessoas)

# Lembrando que o 'while' trabalha da mesma forma que p 'if', sempre busca por verdadeiro ou falso. Por exemplo, para
# se quiser realizar (outro tipo) de 'loop' infinito bastaria colocar 'while True:' ou um operado de comparação.
# OBS: Caso seja colocado por exemplo 'x == 3', o programa acima passará por 'x = 0' depois por 'pessoas []' e
# finalmente irá ler o 'while x == 3:'. Isso mostra que é falso e fará com que o programa ignore as linhas seguintes e
# salte para o 'print (pessoas)'.

# No exemplo abaixo mostra-se como parar um 'loop' caso uma 'string' específica for digitada durante a execução do
# programa
x = 0
pessoas = []

# A linha abaixo significa enquanto a 'string' joao não aparecer (por isso o uso de 'not in') o 'loop' continua
# funcionando. Mas caso seja incluido joao o 'loop' deve parar. E quando ele parar, apresentará a lista de nome.

# O nome joao está na lista, por que não há mecanismos dentro do 'loop' para evitar que o nome joao seja incluso
# a lista, porém isso pode ser feito caso tenha a necessidade.

# Lembre-se que também pode colocar 'if' dentro do 'while'. Como pode ver que há linhas estão comentadas para não
# atrapalhar o exemplo, mas caso queira realizar a não inclusão do nome desejado, basta descomenta-las. Estas linhas são
# parte de um mecanismo para que caso o nome joao seja digitado para incluir na lista, o programa ira reiniciar o 'loop'
# pedindo novamente que digite um nome. Para funcionar descomente as linhas 'while x < 4:', 'if nome == 'joao':',
# 'continue', 'x += 1' e comente (usando '#') 'while 'joao' not in pessoas:'. Desta forma o programa entende que o
# usuário tem que colocar 4 nomes diferentes (ou iguais), mas quando digitado joao o programa voltará ao inicio e
# só irá finalizar quando qualquer outro nome diferente de joao seja incluso.
while x < 4:
#while 'joao' not in pessoas:
    nome = input ('Qual o seu nome? ')
    if nome == 'joao':
        continue
        #break              # O 'break' irá finalizar o 'loop', ou seja, o programa saltará para o 'print'.
    pessoas.append(nome)    #  Para que o 'break' funcione descomente-o e comente o 'continue'.
    x += 1

print (pessoas)