# No python, vários módulos são instalados automáticamente em uma pasta padrão. Esses módulos são chamados de 'built-in'
# e eles podem ser usados sem precisar estar na mesma pasta que o programa a ser rodado.

import math

# O 'math.ceil' faz o arredondamento do valor para cima, por exemplo se algo custa 0.99 será arredondado para 1
my = math.ceil (3.2)
print (my)

# Já para arredondar para baixo usa-se o '.floor'
my = math.floor (3.7)
print (my)

# No arquivo de 'loop for' realizou-se um somatorio para o programa fatura.py, poderia usar um 'built-in' do 'math' para
# fazer a mesma tarefa.
# No exemplo abaixo há uma lista de numeros e o 'math.fsum' irá somar todos os números da lista.
my = math.fsum([1,2,3,4,5,6,7,8,9])
print (my)

# Também pode-se realizar calculos com raiz quadrada
my = math.sqrt (234)
print (my)

# Outro que é muito útil é o 'time', pois ele lida com contagem de tempo, horário e data. Por exemplo, usando o
# 'time.localtime' teremos o resultado mostrado no 'print':

# Estrutura de tempo  Ano           Mês      Dia        Hora       Minuto    Segundo    (------------vide obs-------------)
# time.struct_time(tm_year=2019, tm_mon=8, tm_mday=3, tm_hour=10, tm_min=46, tm_sec=31, tm_wday=5, tm_yday=215, tm_isdst=0)
import time
tempo = time.localtime ()
print (tempo)

# Observações
# tm_wday - Nesta parte é o posicionamento do dia da semana, por exemplo 0 = Segunda Feira, 1 = Terça Feira,
# 2 = Quarta Feira, 3 = Quinta Feira, 4 = Sexta Feira, 5 = Sábado e 6 = Domingo.
# tm_yday - Neste indica quando o dia ano(de forma ordinal).
# tm_isdst - Aqui refere-se ao Horário de Verão.
# O 'time' pode ser usado em várias formas para registro de datas e horas. Um ponto interessante é usar em transações
# ou em registros de pedidos, quando foi recebido a ordem de pedido, de quando ela foi processada e teve a saída para
# entrega.
hora = time.localtime().tm_hour # Note que usou-se 'time.localtime()' para chamar toda a estrutura e também usou o
print (hora)                    # '.tm_hour' para apresentar somente a hora local.
tempo = time.localtime()        # Para não ficar digitando todas as vezes 'time.localtime()', pode-se gerar uma variável
minuto = tempo.tm_min           # e atribuir a chamada ao valor.
print (minuto)
print ('Transação realizada as '+ str(hora)+'h e '+ str(minuto)+' minutos.') # O '+' concatena 'strings'

# Existe uma função dentro do módulo 'time' que é o 'clock'. Esta função é um cronometro. É interessante, pois é usado
# para jogos ou experimentos científicos. Por exemplo, abaixo esta função será usada para contabilizar o tempo que o
# usuário leva para escrever o próprio nome.
def cont_tempo():
    inicio = time.perf_counter()
    input('Escreva seu nome: ')
    fim = time.perf_counter()
    tempo = round(fim - inicio,2) # 'round' é uma função para "arredondar" um número em dízima. Para isso colocou-se um ',2' para duas casa decimais.
    print ('Você levou: '+ str(tempo)+ ' segundos para escrever seu nome!')
cont_tempo()
