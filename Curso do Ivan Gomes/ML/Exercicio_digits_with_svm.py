import warnings
warnings.filterwarnings('ignore')
from sklearn import datasets
digits = datasets.load_digits()

print (digits.data.shape)
print (digits.target.shape)

print (digits.images[128])

import matplotlib
import matplotlib.pyplot as plt
#%matplotlib inline

plt.figure(figsize=(0.5,2))
plt.imshow(digits.images[128], cmap=plt.cm.gray_r)

from sklearn.model_selection import train_test_split
x = digits.data
y = digits.target
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.20,random_state=5)

from sklearn.svm import SVC
classifier = SVC()
classifier.fit(x_train, y_train)
clss_pred = classifier.predict(x_test)
from sklearn import metrics
hits = metrics.accuracy_score(y_test, clss_pred)
print(hits)