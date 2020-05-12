# O uso de módulos externos (não nativos do python) são para auxiliar em outras tarefas ou para complementar os módulos
# built-in. Um dos módulos externos mais conhecidos é o pygames. O download é gratuito.
# Caso esteja sendo usado Windows acesse https://www.pygame.org/wiki/GettingStarted#Windows%20installation e siga as
# intruções de instalação. Se estiver usando Fedora/Red Hat acesse https://www.pygame.org/wiki/GettingStarted#Fedora/Red%20hat.
# Se estiver usando Debian/Ubuntu/Mint acesse https://www.pygame.org/wiki/GettingStarted#Debian/Ubuntu/Mint.

# Comando para instalação do pygame no windows: py -m pip install  pygame -U --user

# WXpython é uma GUI para interfaces (wxpython.org)
# O SQL Alchemy é um módulo para o python interagir com o banco de dados.
# O módulo Beautiful Soup server para extrair conteúdo de páginas da internet.
# O módulo matplotlib é parte do scipy (que é um conjunto de módulos (um ecosistema python)) que faz gráficos.
# Abaixo foi feito um programa para gerar um gráfico para analisar as vendas de um período do ano.

#import matplotlib.pyplot as plt # Aqui a importação do módulo foi resumida para 'plt'

#x = [1,2,3,4,5,6] # Lista do mês do ano no primeiro semestre
#y = [1500,1800,1300,1900,2100,2000] # Lista de vendas feitas no primeiro semestre
legenda = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho']  # Graficos não aceitam 'str' mas pode-se legendar.
plt.xticks (x,legenda)
plt.plot (x,y) # Esta função '.plot' gerá o grafico de acordo com as listas
graf = plt.show() # A função '.show' apresenta o gráfico ao usuário
print (graf)