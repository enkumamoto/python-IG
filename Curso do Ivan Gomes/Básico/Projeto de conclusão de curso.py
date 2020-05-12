print ('Calculadora geométrica')
print ('Com este programa pode-se calcula a área das formas geométricas,\ncomo um triângulo retângulo, um quadrado, um círculo, um trapézio ou um retangulo!\n Não precisa usar acentos na sua escolha!')
print ('Escolha entre as opções abaixo:\n 1 - Triângulo\n2 - Círculo\n3 - Trapezio\n4 - Quadrado\n5 - Retângulo')
pi = 3.14
forma = int(input ('Qual forma você quer calcular a área:'))

if forma == 1:
    print ('Você escolheu calcular a área do triângulo retângulo.\nPressione "Enter" para dar as medidas dos lados do Triângulo.')
    a = float(input ('Digite o valor da base em cm: '))
    b = float(input('Digite o valor da altura  em cm: '))
    tri = (a * b)/2
    print ('A área do triangulo retangulo é: ',tri,'cm²')

elif forma == 2:
    print('Você escolheu calcular a área do círculo.\nPressione "Enter" para dar a medida do raio.')
    c = float(input('Digite o valor do raio em cm: '))
    circ = (pi * c) ** 2
    print('A área do círculo é: ',circ, 'cm²')

elif forma == 3:
    print('Você escolheu calcular a área do trapézio.\nPressione "Enter" para dar as medidas do trapézio.')
    d = float(input('Digite o valor em cm da Base maior: '))
    e = float(input('Digite o valor em cm da base menor: '))
    f = float(input('Digite o valor em cm da altura: '))
    trap = ((d + e)/2) * f
    print('A área do trapézio é: ',trap, 'cm²')

elif forma == 4:
    print('Você escolheu calcular a área do quadrado.\nPressione "Enter" para dar a medida do lado do quadrado.')
    g = float(input('digite o valor em cm do lado do quadrado: '))
    quad = (g ** 2)
    print('A área do trapézio é: ',quad, 'cm²')

elif forma == 5:
    print('Você escolheu calcular a área do retângulo.\nPressione "Enter" para dar as medida da base e da altura.')
    h = float(input('Digite o valor da base em cm: '))
    i = float(input('Digite o valor em cm da altura: '))
    ret = (h * i)
    print('A área do retângulo é: ',ret, 'cm²')

else:
    print ('Opção inválida. Programa encerrado!')