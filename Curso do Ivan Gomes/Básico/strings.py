# Exemplo da aula de string

nome = 'ananda'
sobrenome_mae = "seabra"
sobrenome_pai = 'kumamoto'
print (nome + sobrenome_pai) #concatenação
#len (sobrenome_mae)
nome_completo = nome + ' ' + sobrenome_mae + ' ' + sobrenome_pai
print (nome_completo)
#len (nome_completo)
print (nome)
#len (nome)
iniciais = nome[0] + sobrenome_mae[0] + sobrenome_pai[0]
print (iniciais)
empresa = 'edigitalk'
email = nome + '.' + sobrenome_pai + '@' + empresa + '.com'
print (email)
