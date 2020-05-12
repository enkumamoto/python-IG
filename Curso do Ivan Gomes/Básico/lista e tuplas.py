# Tuplas são imutáveis, ou seja, o que há nela não pode ser mudado
meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
print (meses)
#Listas são mutáveis, ou seja, pode-se acrescentar ou retirar itens da lista.
alunos = ['joao','maria','pedro','helena']
print (alunos)
# Caso queira modificar um item de uma lista, por exemplo o nome de maria foi digitado errado e na verdade ela é mariah,
# deve-se verificar a posição do nome, neste caso está na posição 1 (se estiver usando IDLE) e codificar da seguinte
# maneira:
alunos[1] = 'mariah'
print (alunos)
# Vamos dizer que deve-se acrescentar um novo aluno a lista de alunos, deve-se usar os métodos dentro do python para
# realiza a tarefa. Neste caso será usado a variável alunos seguido de ponto (.) e append:
alunos.append ('ricardo')
print (alunos)
# Como falado, listas são mutáveis e no exemplo acima mostra como incluir um novo dado na lista. Mas também pode
# reposicionar os itens ou colocar um novo dado numa posição de sua escolha usando outro método alunos.insert:
alunos.insert (1,'paula')
print (alunos)