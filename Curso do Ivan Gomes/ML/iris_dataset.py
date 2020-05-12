# Iris Dataset
### Importação dos dados
from sklearn.datasets import load_iris
iris = load_iris()

### Observações
x = iris.data
print(iris.data)
#print(type(iris.data)) #1

### Target #2, 3
y = iris.target
print(iris.target)
#print(iris.target_names)

### Shape das observações e do Target #4
print(iris.data.shape)
print(iris.target.shape)

### Importação do KNN #5
from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier (n_neighbors = 11)

### Treinamento da máquina #6
knn.fit(x,y)

### Previsões #7, 8
species = knn.predict([[5.9,3,55.1,1.8]]) [0]
print (iris.target_names[species])

### Separação dos dados em dois grupos #9, 10
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.50)
#print (x_train.shape)
#print (x_test.shape)
#print (y_train.shape)
#print (y_test.shape)

### Avaliação da performance do modelo #11, 12, 13
knn.fit(x_train,y_train)
predict = knn.predict(x_test)
from sklearn import metrics
hits = metrics.accuracy_score(y_test,predict)
print (hits)

### Aplicação do modelo de regressão logística #14, 15
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression(multi_class="ovr")
logreg.fit(x_train,y_train)
logreg_predict = logreg.predict(x_test)
logreg_hits = metrics.accuracy_score(y_test,logreg_predict)
print (logreg_hits)


# 1 - O tipo do dado enviado pelo iris.data é um 'munpy.ndarray', que quando impresso apresenta algo parecido com uma lista.
# A diferença entre o ndarray e a lista é que o ndarray é bem mais eficiente que a lista, ocupa menos espaço na memória
# e são mais rápidas de percorrer. Além de oferecerem métodos para r ealizar diversas operações vetoriais e matriciais.

# 2 - O Target são os resultados em machine learning, que no caso deste exemplo serão os tipos de plantas. Usando o print
# com da forma acima, os resultados serão apresentado de forma numérica, caso queira ver os nomes das flores após a palavra
# target acrescente '_names'.
# 3 - Lembre-se que para trabalhar com machine learning as observações e os targets devem usar os ndarrays de forma numérica
# e nunca com valores em fomato de string.

# 4 - O (atributo) shape é uma forma de saber se as informações das observações e dos target são iguais. No caso do
# iris.data.shape, apresenta-se 150 observações e 4 atributos (features ou medidas) e no iris.target.shape apresenta 150
# resultados.

# 5 - Neste ponto importa-se o KNN para começar a a valorização do K. Para isso funcionar foram adicionados x = iris.data nas
# observações e y = iris.target no Target.

# 6 - Aqui fez-se o treinamento da máquina. O método knn.fit(x,y) já é preparado para receber as informações no shape das
# observações e do target.

# 7 - Neste ponto começa as previsões pós-treinamento usando o método knn.predict([]). Dentro dos colchetes colocaremos uma
# observação qualquer para testar uma classificação.

# 8 - Transformou knn.predict([]) em valor para species, no final entre [] colocou-se o valor do array e um print para
# (iris.target_names[species]) para saber qual a iris que aparece com os valores da observação.

# 9 - Este módulo é para separar o grupos de dados, poderia ser feito manualmente mas com este módulo a separação será
# realizada com uma linha de código. Precisaremos de duas variáveis x e y, uma vai ser para treinar a máquina e outra para teste.

# 10 - 'x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)' esta linha é que fará o trabalho de separação.
# Lembre-se que o x e y são as observações e o target e o test_size significa o tamanho do teste. O valor de 0.25 significa que
# o teste usará 25% das informações para teste e os 75% restantes para treinamento. Quanto mais dados para treinamento melhor.

# 11 - Aqui usaremos o knn.fit usando o x_train e y_train e também criou-se uma variável com valor knn.predict que receberá
# vários valores ao mesmo tempo, no caso usaremos o x_test. Com o output de predict basta realizar uma comparação com y_test.

# 12 - o 'from sklearn import metrics' importará um metodo de análise estatística e o 'hits = metrics.accuracy_score(y_test,predict)'
# mostrará a porcetagem de acerto realizados pelo modelo.

# 13 - O resultado da previsão pode mudar, pois o teste busca 25% dos dados de forma aleatória.
# Será usado uma parte de estatística para que o treinamento da máquina seja bem feito, será usado o KNN (K Nearest Neighbors).

# 14 - Quando se trabalha com mais variáveis, deve-se pensar da forma One vs All, assim o programa conseguirá analisar as informações
# e tratar cada uma delas e comparar os resultados das outras análises, ao fim das comparações o maior resultado é dado como
# é dado como verdadeiro. Por exemplo, temos as flores da espécie A, B e C. Considerando que cada uma delas tem pétalas com
# tamanho padrão, a espécie A tem medidas QWER, B tem medidas SDFG e C tem medidas HJKL. Realizou-se a médida de uma amostra
# e inseriu os dados para análise. O que vai acontecer é que o programa irá analizar as medidas inseridas e irá verificar os padrões
# e no final apresentará um resultado aproximado (em porcentagem) se a amostra é da espécie A, B ou C.

# 15 - Usando o logreg.predict será apresentado o resultado de forma direta de acordo com a probabilidade mais alta, mas
# se usar o logreg.predict_proba serão apresentadas as probabilidade (em porcentagem) no formado One vs All.

# A ideia principal do KNN é determinar o rótulo de classificação de uma amostra baseado nas amostras vizinhas advindas
# Para determinar a classe de um elemento que não pertença ao conjunto de treinamento, o classificador KNN procura K elementos
# do conjunto de treinamento que estejam mais próximos deste elemento desconhecido, ou seja, que tenham a menor distância.
# Estes K elementos são chamados de K-vizinhos mais próximos. Verifica-se quais são as classes desses K vizinhos e a classe
# mais freqüente será atribuída à classe do elemento desconhecido.

# Neste código também será usado a Regressão Logística, é usado em ML para previsões categóricas. É bem usado para saber
# se um e-mail é spam ou não, se um tumor é maligno ou benigno, esses dois exemplo são previsões categoricas binárias, ou seja
# a resposta da análise é um ou outra coisas. No caso do iris dataset é categórico de multi espécies, ou seja, 3 ou mais
# respostas diferentes. A Regressão Logística deve ser usada em classificação binária, mas não impede de usar com mais
# variáveis.

