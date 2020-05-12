# Dicionário é um conjunto de valores ( como listas e tuplas), mas que não tem uma sequência ordenada.
# Não pode acessar os valores dos diciónarios por meio de índices. E o acesso é por meio de keys (chaves '{}').
joao = {'nome' : 'joao', 'sobrenome' : 'pereira', 'profissao' : 'programador python', 'filhos' : ['pedro','maria']}

# Dicionários não tem índices numéricos, a não ser que seja definido anteriormente.
print (joao ['sobrenome'])
print (joao ['profissao'])
print (joao ['filhos'])

# Na linha abaixo, mostra a quantidade de itens no dicionário.
# OBS: o print está sendo usado para apresentar o resultado do len no pycharm e não há necessidade de usa-lo no IDLE.
print (len(joao))

# Para deletar alguma informação do dicionário deve usar 'del' o nome do dicionário seguido do que deseja remover do
# dicionário, por exemplo filhos.
del joao ['filhos']
print (joao)

# Lembre-se que dicionários são mutáveis e pode-se manipular as informações nele da forma que quiser. Por exemplo,
# se quer mudar a profissão do usuário:
joao ['profissao'] = 'aposentado'
print (joao)

# Caso tenha a necessidade de procurar alguma chave específica, basta digitar a key seguido de 'in' e o nome do dicionário.
# se a keys existe dentro do dicionário, retornará 'True' se não retornará 'False'
print ('sobrenome' in joao)
print ('idade' in joao)

# Loop é algo que é importante para algumas coisa no python e é usado bastante em dicionários.
# No caso abaixo o loop 'for' com x e 'in' joao, fará uma percorrer o dicionário joao, onde 'x' são todas as chaves
# e com o print (x) ele mostrará na tela todas as chaves do dicionário.
for x in joao:
    print (x)

# Também pode-se imprimir todas as chaves com detalhes, caso seja necessário.
# Isso é feito por meio de concatenação. O que deve ser feito é incluir o "(x+':' +joao[x])" que quer dizer que ele
# deve pedir o 'x' mais o texto do ':' e concatenar o dicionário joao para que todas as vezes que ele passar pelas chaves
# ele mostre as informações.
for x in joao:
    print (x+': '+joao[x])

# Pode-se usar o método 'get' para buscar alguma informação dentro do dicionário, como por exemplo o nome. Isso pode
# fazer retornar algum texto caso não encontre a informação que procura. O que a linha abaixo irá fazer é procurar a
# chave nome, achando a chave nome será mostrado o valor desta chave. Se a chave não existir retornará a mensagem em
# vez de um erro.
print (joao.get('nome', 'Esta informação não consta no cadastro'))

# Abaixo mostra-se um caso de "erro" onde não há idade no dicionário, então será mostrada a mensagem.
print (joao.get('idade', 'Esta informação não consta no cadastro'))

# Devolvendo os filhos a lista de chaves
joao['filhos'] = ['pedro','maria']
print (joao)

# Caso um chave precise de atualização nos valores pode-se usar o '.append' na chave e em seguida atribuir o novo valor.
# no caso da chave filhos o valor dela é uma lista (vide arquivo 'listas e tuplas') assim facilitando o processo.
joao ['filhos'].append('jorge')
print (joao)

# Para limpar o dicionári usa-se '.clear'. Quando executado verá que o dicionário existe mas está vazio. Assim pode
# readicionar as informações ou novos dados.
joao.clear ()
print (joao)