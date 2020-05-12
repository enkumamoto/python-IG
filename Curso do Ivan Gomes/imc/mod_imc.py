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