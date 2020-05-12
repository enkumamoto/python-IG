# Comece um novo programa e crie um dicionário de cores em inglês. Em seguida, peça ao usuário para digitar uma cor
# em português. Caso exista a cor no dicionário, imprima a tradução, caso contrário, imprima algo como "Esta cor não
# existe no meu dicionário".

cores = {'vermelho':'red', 'azul': 'blue', 'verde':'green', 'preto': 'black', 'laranja':'orange'}
print ('Bem vindo ao tradutor de cores!')

# Caso o usuário digite a primeira letra maiúscula o programa dará erro. Então usando o método '.lower()', independente
# do usuário escrever como letras maiúsculas ou não, o .lower deixará o input (com strings) em minúsculo.
cor = input('Digite a cor que quer traduzir: ').lower()

traducao = cores.get(cor, 'Esta cor não existe no meu dicionário! =(')
print (traducao)