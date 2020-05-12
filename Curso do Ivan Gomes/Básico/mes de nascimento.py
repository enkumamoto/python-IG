# Programa para dizer o seu mês de nascimento

meses = ('janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro')
nasc = input('Digite a sua data de nascimento no formato DD-MM-AAAA: ')

# Na linha abaixo há um slice, onde mostra-se 3:5, que quer dizer que o slice deve buscar o dado entre a posição 3 e 5.
# Neste caso foi dito que o o slice de um número inteiro de DD-MM-AAAA deve ser buscado e realizar a subtração de 1
# para apresentar o mês correto ao usuário. Por isso que usa-se 'indice = int(nasc[3:5])-1'.
# Lembre-se que o número 0 conta.
indice = int(nasc[3:5])-1
mes = meses[indice]

print('Você nasceu no mês de',mes)