# Programa para checagem de IMC
def imc(peso,altura):
    imc = peso /(altura*altura)
    return imc

def class_imc (sexo,peso,altura):
    valor_imc = imc(peso,altura)
    if sexo == 'm':
        if valor_imc < 20.7:
            return ('Sibito Baleado.')
        elif valor_imc >= 20.7 and valor_imc < 26.4:
            return ('Pia o mago se achando gordo.')
        elif valor_imc >= 26.4 and valor_imc < 27.8:
            return ('E ai, gordin?! Procure um(a) nutricionista para te recomendar uma dieta legal e comece a se exercitar!')
        elif valor_imc >= 27.8 and valor_imc < 31.1:
            return ('gordo! Procure um(a) nutricionista para te recomendar uma dieta legal e comece a se exercitar!')
        elif valor_imc >= 31.1 and valor_imc < 350:
            return ('Já pensou numa baritrica ou numa funeraria?')
        else:
            return 'Erro de cálculo. Entre em contato com o adiministrador.'

    if sexo == 'f':
        if valor_imc < 19.1:
            return ('Sibito Baleado.')
        elif valor_imc >= 19.1 and valor_imc < 25.8:
            return ('Pia mermo, o maga se achando gorda.')
        elif valor_imc >= 25.8 and valor_imc < 27.3:
            return ('E ai, gordin?! Procure um(a) nutricionista para te recomendar uma dieta legal e comece a se exercitar!')
        elif valor_imc >= 27.3 and valor_imc < 32.3:
            return ('gorda!  Procure um(a) nutricionista para te recomendar uma dieta legal e comece a se exercitar!')
        elif valor_imc >= 32.3 and valor_imc < 350:
            return ('Já pensou numa baritrica ou numa funeraria?')
        else:
            return 'Erro de cálculo. Entre em contato com o adiministrador.'

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

v_imc = str(imc (peso,altura))
c_imc = class_imc(sexo,peso,altura)

print ('Olá '+nome+'!')
print ('O seu IMC é: %0.2f'%v_imc)
print ('A sua classificação é: ',c_imc)
