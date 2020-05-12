# Um módulos são arquivos '.py', ou seja cada programa feito é um módulo independente. O que acontece é que esses
# módulos podem se conectar para exapadir as possibilidades dentro do python. Para exemplificar usou-se o programa
# 'imc.py' onde será separado as funções do programa e colocadas em outro arquivo e a parte interativa neste arquivo.
# Como pode ser visto nas variáveis 'v_imc' e 'c_imc' elas usam as funções que não estão dentro do programa. O que
# deve fazer é usar o comando 'import' seguido do nome do módulo, que foi nomeado como 'mod_imc'. As vezes o módulo
# pode ter um nome muito grande, então pode "renomea-lo" usando a expressão 'as "X"'. Em caso do uso deve-se lembrar
# que onde há chamadas do módulo deve ser alterado para a forma renomeada.

import mod_imc as m_i

print ('Bem vindo ao ChecaPeso!')
print ('Aqui você fica sabendo se voce precisa de ajuda')
print ('para saber se voce precisa de ajuda com dieta,')
print ('academia ou se você precisa de uma bariátrica!')
nome = input ('Digite seu nome: ').title()
print ('\n') # Nesta linha, realiza uma quebra de linha usando '\n'
valid_sex = False
while valid_sex == False:
    sexo = input('Digite seu sexo usando F ou M: ').lower()
    if sexo != 'm' and sexo != 'f':
        print ('Sexo inválido, digite F ou M')
    else:
        valid_sex = True
        print ('\n')
valid_peso = False
while valid_peso == False:
    peso = input('Digite seu peso (Ex.:65.7): ')
    try:
        peso = float(peso)
        if peso <= 0 or peso > 595:
            print ('Peso inválido. Número não pode ser zero ou negativo e deve ser inferior que 350.')
        else:
            valid_peso = True
            print('\n')
    except:
        print('Peso inválido. Use apenas números e separe os decimais com ponto. (Ex. 9.5)')
valid_alt = False
while valid_alt == False:
    altura = input('Digite sua altura (Ex. 1.78): ')
    try:
        altura = float(altura)
        if altura<= 0 or altura > 3:
            print ('Peso inválido. Número não pode ser zero ou negativo e superior a 3')
        else:
            valid_alt = True
            print ('\n')
    except:
        print('Altura inválida. Use apenas números e separe os decimais com ponto. (Ex. 1.84)')

# Para que o módulo funcione devidamente devese colocar nas linhas abaixo o nome do módulo criado.
v_imc = str(m_i.imc (peso,altura))
c_imc = m_i.class_imc(sexo,peso,altura)

print ('Olá '+nome+'!')
print ('O seu IMC é: %0.2f'%v_imc)
print ('A sua classificação é: ',c_imc)