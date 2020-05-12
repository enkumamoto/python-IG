# Uma das coisas que podem ser feitas usando este módulo é realizar pedidos a algumas apis na internet que retornam
# dados e trabalhar no programa. HTTP realiza transferencia de dados na internet. Este programa irá pedir a um serviço
# que vai reconhecer a localização baseado no endereço de IP e com a localização o programa fará um outro pedido para
# uma segunda api de meteorologia que apresentará a temperatura atual da localização.
# Antes de começar a escrever o programa, deve-se pesquiser apis que retornem as informações gratuitamente. Por exemplo
# a 'developer.accuweather.com' e a 'geoplugin.com'.
# O código da api que será usado será em formato JSON (é um dicionário popular de python).
# A idéia deste programa será reconhecer o ip que está sendo usado e que a própria api traga a lozalização retornando a
# latitude e longitude do usuário.
# Se colocarmos 'type (r.text)' o python nos dirá que é uma "class 'str'" porque estamos usando JSON. O JSON significa
# JavaScript Object Notation e é como um objeto javascript fosse um dicionário em python. Em outras palavras JSON para
# python são dicionários ou listas convertidas para strings. A vantagem dessa conversão é enviar os dados para ser usado
# em qualquer linguagem de programação.
# Recomenda-se o uso do pprint para organizar de uma melhor forma o dicionário para entender melhor os dados.
# AccuWeather APIkey -  NP3Amhm0ud2NrTtJLnuWTpHd2RthOOUH
# Código da localização a ser usada: 2725728
# A API do Accuweather não aceita latitude e longitude, com isso deve-se usar um código do local para que a API puxe
# informações meteoroligas do país que ele irá atuar.

import requests
import json
#import pprint

acwapik = 'NP3Amhm0ud2NrTtJLnuWTpHd2RthOOUH'

r = requests.get ('http://www.geoplugin.net/json.gp')   # Requisição feita ao geoplugin.com.
if (r.status_code != 200):                              # Verificando se o site está funcionando normalmente.
    print ('Não foi possível obter sua localização.')   # Se NÂO estiver funcionando, será apresentado a mensagem.
else:                                                   # Caso o site esteja funcionando será apresentado o código em JSON
    local = json.loads(r.text)                          # Converter o código em dicionário para o python.
                                                        # Retorna o r.text de forma organizada. Note que o dicionário
                                                        # é de um nível e cada item é uma chave.
    lat = local['geoplugin_latitude']                   # Aqui usaremos a latitude fornecida pelo geoplugin (entre [''])
    long = local['geoplugin_longitude']                 # Aqui usaremos a longitude fornecida pelo geoplugin (entre [''])
    #print(pprint.pprint(local))
    localapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
    + "search?apikey=" + acwapik \
    + "&q=" + lat + "%2C"+ long + "&language=pt-br"

    r2 = requests.get(localapiurl)
    if (r2.status_code != 200):
        print ('Não foi possível obter o código do local.')
    else:
#       print (pprint.pprint(json.loads(r2.text))       # Esta linha apresenta as informações do accuweather organizada
                                                        # e está comentada pois era usada para testes.
        localresponse = json.loads(r2.text)             # Vide linha 30

        # Na linha abaixo criou-se uma variável para que retorne no programa o nome da cidade, estado e país.
        # Foi usado 'ParentCity' na primeira parte pois estava pegando o nome do bairro e não da cidade.
        nomelocal = localresponse['ParentCity']['LocalizedName']+', ' \
                    + localresponse['AdministrativeArea']['LocalizedName']+'. ' \
                    + localresponse['Country']['LocalizedName']
        codlocal = localresponse['Key']
        print('Obtendo clima de :', nomelocal)
#       print('Código do Local:', codlocal)             # Apresenta o código do local
        correntconditionapiurl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                                 + codlocal + "?apikey=" + acwapik \
                                 + "&language=pt-br"
        r3 = requests.get(correntconditionapiurl)
        if (r3.status_code != 200):
            print ('Não foi possível obter o código do local.')
        else:
            currentconditionresponse = json.loads(r3.text)
#            print (pprint.pprint(currentconditionresponse))
            textoclima = currentconditionresponse [0]['WeatherText']
            temperatura = currentconditionresponse[0]['Temperature']['Metric']['Value']
            print ('O clima está: '+textoclima)
            print ('A temperatura é de: ' +str(temperatura) +'°C')