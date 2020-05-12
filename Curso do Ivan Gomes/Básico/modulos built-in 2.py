# Abaixo importou-se o módulo 'random' para tratar de números aleatórios
import random
ale = random.randint (0,10) # O '.randint' utilizará uma 'range' determinado pelo usuário, no caso de 0 - 10,
print (ale)                 # ou seja, será apresentado aleatoriamente números de 0 - 10.

# Por exemplo, foi pedido para criar um programa para gerar números para jogos da mega sena. Para isso cria-se uma
# lista vazia para ela ser preenchida a cada passagem, para isso cria-se um 'loop while'.
def megasena():
    jogo = []
    while len(jogo) < 6: # Aqui mostra que o jogo da mega sena não pode ter menos de 6 números
        num = random.randint (1,60) # Aqui dentro do 'loop' a variável tem seu valor números randomicos de 1 a 60
        if num in jogo: # Nesta condicional mostra que o 'loop' deverá gerar 6 números para o jogo e preencher a lista,
            continue    # quando esta lista finalizar, o programa irá saltar para o 'print' que apresentará a lista
        else:           # de forma ordinal (com o uso do 'sorted').
            jogo.append(num) # Caso um número se repita dentro do 'loop' o programa retorna para o inicio do 'loop',
    print(sorted(jogo))      # caso o número aleatório não
megasena()                   # esteja na lista ai sim será usado o '.append'.

# Com o módulo choice pode-se usar aleatoriamente itens de uma lista
alunos = ['joao','pedro','maria','helena','guilherme','carla','jose','marcos']
cast = random.choice(alunos)
print (cast)

# o 'random.sample' proporciona uma amostra de dentro de uma lista. Esta função pode ser usada para estatística. O que
# precisa ser feito é apresentar a quantidade para o 'sample' e a cada passagem será pego novamente a quantidade
# desejada aleatoriamente.
cast = random.sample (alunos,3)
print (cast)

# Os módulos pythom estão dentro da pasta 'lib' e caso seja feito um módulo que não nativo, basta sava-lo dentro desta
# pasta e realizar o import como um módulo nativo. Também pode visualizar os módulos (abri-los e ver a estrutura).
# Alguns módulos, como o math, não estão dentro da pasta lib pois já estão integrados ao python.
# Acessando a documentação do Python, poderá achar a listagem dos módulos e suas funções.
