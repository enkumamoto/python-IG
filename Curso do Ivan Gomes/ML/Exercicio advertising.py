import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

tests = [['TV', 'radio', 'newspaper'],['TV', 'radio'],['TV', 'newspaper'],['radio', 'newspaper']]
winner = {'test': '','Performance': None}
first_pass = True

publi = pd.read_csv('http://faculty.marshall.usc.edu/gareth-james/ISL/Advertising.csv',index_col=0)

for test in tests:
    x = publi[test]
    y = publi['sales']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.50, random_state=5)
    reglin = LinearRegression()
    reglin.fit(x_train, y_train)
    y_prev = reglin.predict(x_test)
    rmse = np.sqrt(metrics.mean_squared_error(y_test,y_prev))
    print('Test: ')
    print(test)
    print('Performance: ')
    print(rmse)
    print('--------------')
    if (first_pass):
        winner['test'] = test
        winner['performance'] = rmse
        first_pass = False
    else:
        if (rmse < winner['performance']):
            winner['test'] = test
            winner['performance'] = rmse

print('--------------')
print('Winner: ')
print(winner['test'])
print("Winner's Performance:")
print(winner['performance'])