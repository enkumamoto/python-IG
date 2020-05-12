from sklearn import datasets
digits = datasets.load_digits() #1

print (digits.data.shape) #2
print (digits.target.shape) #2

#print (digits.data[0]) #3
print (digits.images[0]) #3

import matplotlib.pyplot as plt
#%matplotlib inline #4

plt.figure(figsize=(2,2))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)

# 1 - esse conjunto de dados consiste em imagens de digitos de 0 a 9 escritos a mão, ou seja programa irá reconhecer
# cada número escrito.
# 2 - o date e o target ira apresentar 1797 amostrar de observações com 64 variáveis.
# 3 - Aqui será apresentado números de 0 a 16 que representam uma cor na escala de cinza (todos os 0 representam a cor
# branca e todos os 16 representam preto). percebe-se que são 64 variáveis detro de uma lista que só farão sentido dentro
# de uma imagem de 8x8 pixels. então para uma melhor visualização, troca-se o digits.data por digits.images. com o
# digits.images a visualização é exatamente como é a imagem.
# 4 - Este é um comando para visualizar o gráfico pelo jupyter notebook.