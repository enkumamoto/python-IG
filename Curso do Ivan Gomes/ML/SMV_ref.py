import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import metrics
import numpy as np
import matplotlib.image as mpimg

digits = datasets.load_digits()

print (digits.data.shape)
print (digits.target.shape)

#print (digits.data[0])
print (digits.data[0])

#%matplotlib inline

plt.figure(figsize=(2,2))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)

x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.01,random_state=5)

classifier = SVC()
classifier.fit(x,y)
#clss_pred = classifier.predict(x_test)
#hits = metrics.accuracy_score(y_test, clss_pred)
#print(hits)
path = #Put the file path here // Coloque o caminho do arquivo aqui
#img = mpimg.imread('Put the file path here // Coloque o caminho do arquivo aqui') #1
img = mpimg.imread(path)
#print (img) #2

def rgb2gray(rgb): #3
    img_array = np.dot(rgb[...,:3],[0.299,0.587,0.114]) #4
    img_array = (16 -(img_array * 16)).astype(int) #5
    img_array = img_array.flatten() #6
    #print(img_array)
    return img_array

clss_pred = classifier.predict([rgb2gray(img)])
print (clss_pred)

# 1 - Duas formas de apresentar os arquivos: 1- Colocando no diretório do jupyter ou 2 - Apontando
# o diretório do arquivo.
# 2 - O output da imagem por sair em RGB e o resultado deverá ser convertido para escala de cinza.
# 3 - Esta função converte de RGB para Gray Scale
# 4 - Nesta parte foi usada fatores multiplicadore para converter o Vermelo, Verde e Azul para escala
# de cinza
# 5 - Aqui uma operação usando '16 - ' e multiplicamos os valores do output por 16, entre parenteses, e usamos o astype
# para convertes todos os resultados em números inteiros.
# 6 - O método flatten converte a matriz 8x8 em output linear para que as features combinem com as do digits.