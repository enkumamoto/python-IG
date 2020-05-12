# O SVM é um algorítimo de ML supervisionado usado para criar limites entre grupos de dados. Por exemplo se tivermos dois
# elementos num gráfico e quisermos classificar uma nova observação. Usando o método kKN essa nova observação seria analisada
# de acordo com o número de vizinhos mais próximos. Já o SVM traça uma linha divisória entre os dois grupos, a partir disso
# o SVM encontra a posição da linha que dê a maior distância entre a linha e os pontos mais próximos de cada lado. A linha
# que divide os grupos é chamada de hyperplane e a soma das duas distância é chamada de margin.
# Lembre o SVM realiza previsões categoricas.

import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets
digits = datasets.load_digits()

print (digits.data.shape)
print (digits.target.shape)

#print (digits.data[0])
print (digits.images[0])

import matplotlib.pyplot as plt
#%matplotlib inline

plt.figure(figsize=(2,2))
plt.imshow(digits.images[0], cmap=plt.cm.gray_r)

from sklearn.model_selection import train_test_split
x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.10,random_state=5)

from sklearn.svm import SVC
classifier = SVC()
classifier.fit(x_train, y_train)
clss_pred = classifier.predict(x_test)
from sklearn import metrics
hits = metrics.accuracy_score(y_test, clss_pred)
print(hits)