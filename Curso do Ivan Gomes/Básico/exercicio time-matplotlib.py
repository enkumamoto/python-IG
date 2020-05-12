import time as t
import matplotlib.pyplot as plt

tempos = []
vezes = []
legenda = []
vez = 1
repete = 3

print ('Este programa marcará o tempo gasto para digitar a palavra PROGRAMÇÃO. Você terá que digita-la '+str(repete)+' vezes.')
input ('Aperte enter para começar.')

while vez <= repete:
    inicio = t.perf_counter ()
    input ('Digite a palavra: ')
    fim = t.perf_counter ()
    tempo = round(fim - inicio,2)
    tempos.append (tempo)
    vezes.append (vez)
    vezstr = str(vez)+'a vez'
    legenda.append(vezstr)
    vez += 1

#legenda = ['1a vez','2a vez','3a vez','4a vez','5a vez']
plt.xticks(vezes,legenda)
plt.plot (vezes,tempos)
graf = plt.show()
print (graf)
print ('Fim do programa.')