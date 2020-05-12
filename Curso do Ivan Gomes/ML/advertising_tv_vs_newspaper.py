import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

publi = pd.read_csv('http://faculty.marshall.usc.edu/gareth-james/ISL/Advertising.csv',index_col=0)
check = publi.head()
print (check)
#print (type(publi))
#print (publi.shape)

x = publi[['TV', 'newspaper']]
y = publi['sales']

#sns.pairplot(publi, x_vars=['TV', 'newspaper'], y_vars='sales', size=3, kind='reg')
graph = sns.pairplot(publi, x_vars=['TV', 'newspaper'], y_vars='sales', size=3, kind='reg')
plt.show(graph)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.50,random_state=5)
reglin = LinearRegression()
reglin.fit(x_train, y_train)

print(list(zip(['TV', 'newspaper'],reglin.coef_)))

y_prev = reglin.predict(x_test)
#print(y_prev)
#print(y_test)


## Avaliação da Performance
### MAE (Mean Absolute Error)
print(metrics.mean_absolute_error(y_test,y_prev))

### MSE (Mean Squared Error)
print(metrics.mean_squared_error(y_test,y_prev))

### RMSE (Root Mean Squared Error)
print(np.sqrt(metrics.mean_squared_error(y_test,y_prev)))