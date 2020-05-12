import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np

publi = pd.read_csv('http://faculty.marshall.usc.edu/gareth-james/ISL/Advertising.csv',index_col=0)  # 1
check = publi.head()  # 2
print (check)
# print (type(publi))  # 3
# print (publi.shape)

x = publi[['TV', 'radio', 'newspaper']]  # 4
y = publi['sales']  # 5

sns.pairplot(publi, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=3, kind='reg')  # 6
# graph = sns.pairplot(publi, x_vars=['TV', 'radio', 'newspaper'], y_vars='sales', size=3, kind='reg')
# plt.show(graph)
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.50,random_state=5)
reglin = LinearRegression()
reglin.fit(x_train, y_train)

print(list(zip(['TV', 'radio', 'newspaper'],reglin.coef_)))  # 7

y_prev = reglin.predict(x_test)  # 8
# print(y_prev)
# print(y_test)
# print(reglin.predict([[230.1, 37.8,69.2]]))

# #  Avaliação da Performance
# # #  MAE (Mean Absolute Error)
print(metrics.mean_absolute_error(y_test,y_prev))

# # #  MSE (Mean Squared Error)
print(metrics.mean_squared_error(y_test,y_prev))

# # #  RMSE (Root Mean Squared Error)
print(np.sqrt(metrics.mean_squared_error(y_test,y_prev)))

#  1 - Esta linha mostra a captura dos dados através de um arquivo CSV. Este arquivo csv contém dados para cruzar o fluxo
#  de vendas vs por meio de publicidade. Este arquivo é formado por 200 linhas x 5 colunas. O pandas gera automaticamente
#  coluna de índece, então para retirar a primeira coluna usa-se index_col=0 (o 0 representa a coluna que quer eliminar)

#  2 - Mostra as primeiras 5 linhas do arquivo, cada linha é uma campanha e cada coluna é o valor gasto em cada meio de
#  comunicação sendo a última a coluna das vendas.

#  3 - O tipo da informação é pandas.core.frame.DataFrame

#  4 - Variável x são as observações

#  5 - Variável y é o target

#  6 - Esta linha nos mostrará os gráficos com um dimensionamento maior e apresentara a linha de regressão. E os gráficos
#  mostram que há aumento de vendas com investimento em propaganda. Vemos que é uma relação positiva com análise na inclunação
#  das linhas, ou seja, temos uma relação forte entre as variáveis. O uso do 'random_state=' ajuda com a previsão durante
#  a reorganização aleatoria dos dados usados

#  7 - coef é uma convenção para coeficiente de regressão linear. Usou-se o list e o zip para melhorar a visualização dos
#  coeciscientes.

#  8 - Criando a variável y_prev para uma previsão usando os dados de x_test e verificar todas as previsões das vendas.
#  Se observar a relação entre y_prev e y_test verá que o valor da segunda coluna de y_test dará aproximado aos valores
#  dos resultados de y_prev.

#  Regressão Linear é um modelo usado para previsões quantitativas. Esta analise quantitativa é dada em dois eixos sendo um
#  com variável independente e outro com variável dependente. Isso fará entender a relação nas duas variáveis, a idéia é se
#  alterar o valor de X (para mais ou para menos) e conseguir relacionar esses valores, saberemos qual o valor de Y baseado
#  no valor de X. A melhor forma de realizar este proceso é usando o 'Least Squares Method' que chega a uma linha que produz
#  o menor erro possível. Esta linha pode apresentar erros e chamaremos os erros de 'e'. Esses erros apresentam a distância
#  entre valor da linha e o valor real da observação. Se elevar todos os erros ao quadrado e soma-los, teremos o valor do
#  erro total da linha. Com isso, como já foi dito, esse resultado nos dará o valor do menor erro possível e com ele teremos
#  como realizar previsões.

#  MAE (Mean Absolute Error) é um método para avaliação de performance que pega os erros e vai tirar uma média dos erros.

#  MSE (Mean Squared Error) é um método que todos os erros ao quadrado para aumentar o peso do erro para melhorar a precisão.

#  RMSE (Root Mean Squared Error) este método pega o resultado do MSE e aplica uma raiz quadrada para converter o resultado
#  em unodade de vendas (para este caso que envolve vendas). Uma observação é que usou-se o numpy para realizar a operação
#  de raiz quadrada, pois o metrics não consegue realiza-lo.

#  O fato de estar trabalhando com várias variáveis pode gerar uma "confusão" na maquina durante a análise. Observando os
#  gráficos gerados pelo programa vê-se que proganda em jornal tem retorno menor que os outros veículos de comunicação, com
#  isso é interessante cruzar as informações entre dois do três para que a precisão das previsões sejam maiores.