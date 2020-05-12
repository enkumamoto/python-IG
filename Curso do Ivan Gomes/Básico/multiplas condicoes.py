# Pode trabalhar com multiplas condições. No caso abaixo as multiplas condições irão verificar de o homem ou
# a mulher é ou não maior de idade.
# Abaixo podemos ver que o código fica muito longo para tomadas de decisões:
idade = int(input('Digite sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()
if idade < 18 and sexo == 'm':
    print ('Homem menor de idade!')
elif idade >= 18 and sexo == 'm':
    print ('Homem maior de idade!')
elif idade < 18 and sexo == 'f':
    print ('Mulher menor de idade!')
elif idade >= 18 and sexo == 'f':
    print ('Mulher maior de idade!')
else:
    print ('Erro na entrada de dados.')

# Para resumir o código e ficar maus limpo
idade = int(input('Digite sua idade: '))
sexo = input('Digite o sexo M ou F: ').lower()
cidade = input('Digite sua cidade: ').lower()

# O 'or' é parecido com o 'and' a diferença é que o 'or' necessita que as duas condições sejam verdadeiras. Para
# exemplificar o 'or' será colocado que o programa realize o teste de idade e gênero só para algumas cidades onde o
# programa roda, vamos testar com três cidades: João Pessoa, Natal e São Paulo, mas o programa só funcionará na região
# nordeste. Caso a cidade a escolha for São Paulo, o programa passará direto para a ultima linha.
if cidade == 'joao pessoa' or cidade == 'recife':

# OBS: A nota abaixo foi feita antes da inclusão do 'or'.
# Abaixo colocou-se um 'if' para identar mais decisões dentro dele mesmo. como pode ver, temos um 'if' com um
# segundo 'if' seguido de um 'else'. Assim o que acontece é, se caso a primeira opção de gênero for feminino (f) a
# primeira linha ignora, saltará para a próxima checagem no 'elif', sendo verdadeiro o programa checará a idade na
# identação do 'if' se for menor que o valor ele saltará para o 'else'. A lógica é a mesma caso a opção seja
# masculino (m).
    if sexo == 'm':
        if idade < 18:
            print ('Homem menor de idade da região nordeste!')
        else:
            print('Homem maior de idade da região nordeste!')
    elif sexo == 'f':
        if idade < 18:
            print ('Mulher menor de idade da região nordeste!')
        else:
            print('Mulher maior de idade da região nordeste!')
    else:
        print('Erro na entrada de dados.')
else:
    print ('Teste apenas para a região Nordeste.')
