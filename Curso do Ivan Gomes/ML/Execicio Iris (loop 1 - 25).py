from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import matplotlib.pyplot as plt

iris = load_iris()
x = iris.data
y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)

values_performance = {}
k = 1

while k <= 25:
    knn = KNeighborsClassifier (n_neighbors = k)
    knn.fit(x_train, y_train)
    predict = knn.predict(x_test)
    hits = metrics.accuracy_score(y_test,predict)
    values_performance [k] = round(hits,4)
    k += 1
print (values_performance)

plt.plot (list(values_performance.keys()),list(values_performance.values()))
plt.xlabel('K Value')
plt.ylabel('Performance')
plt.show()
