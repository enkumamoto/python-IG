# Este programa teve um "refactoring", todos os comentários estão em no arquivo "localizacao_do_usuario.py".
# Neste há novos comentários pertinentes ao processo de remodelação e organização do código.
# Nesta remodelação o programa apresentará a previsão para os próximos 5 dias e pegar a localização pelo ip do usuário.
import requests
import json
#import pprint
from datetime import date
import urllib.parse

acwapik = "MMw4pGhDAqUMWnZAnjtYZScGtflX7xSX"
mbtoken = 'pk.eyJ1IjoiZWlqaWt1bWFtb3RvIiwiYSI6ImNrMXNlMnh4NTBmMm4zY283M2dvY2k1bnIifQ.TBDxdUZJcxorSMfQ841rzw'

week = ["Domingo","Segunda Feira","Terça Feira","Quarta Feira","Quinta Feira","Sexta Feira","Sábado"]

def getcoords():                                                # Função para pegar localização baseada no ip
    r = requests.get ("http://www.geoplugin.net/json.gp")
    if (r.status_code != 200):
        #print(r)
        print ("Não foi possível obter sua localização.")
        return None                                             # Aqui fará que com que o erro não apareça
    else:                                                       # Se a base com ip não funcionar saltará para este ponto
        try:
            local = json.loads(r.text)
            coords = {}
            coords["lat"] = local["geoplugin_latitude"]         # Convertendo "lat" e "long" em dicionário
            coords["long"] = local["geoplugin_longitude"]
            #print(pprint.pprint(local))
            return coords
        except:
            return None

def getlocalcod(lat, long):                                     # Nesta função tem dois argumentos para retornar o código do local.
    localapiurl = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/" \
    + "search?apikey=" + acwapik + "&q=" + lat + "%2C"+ long + "&language=pt-br"

    r = requests.get(localapiurl)
    if (r.status_code != 200):
        #print(r)
        print ("Não foi possível obter o código do local.")
        return None
    else:
        try:
            localresponse = json.loads(r.text)
            localinfo = {}
            localinfo["localname"] = localresponse["ParentCity"]["LocalizedName"] + ", " \
                                     + localresponse["AdministrativeArea"]["LocalizedName"] + ". " \
                                     + localresponse["Country"]["LocalizedName"]
            localinfo ["localcod"] = localresponse["Key"]
            return localinfo
        except:
            localresponse = json.loads(r.text)
            localinfo = {}
            localinfo["localname"] = localresponse["LocalizedName"] + ", " \
                                     + localresponse["AdministrativeArea"]["LocalizedName"] + ". " \
                                     + localresponse["Country"]["LocalizedName"]
            localinfo["localcod"] = localresponse["Key"]
            return localinfo

def getinfoweathernow(localcod,localname):                      # Nesta função tem o código e o nome do local.
    correntconditionapiurl = "http://dataservice.accuweather.com/currentconditions/v1/" \
                             + localcod + "?apikey=" + acwapik + "&language=pt-br"
    r = requests.get(correntconditionapiurl)
    if (r.status_code != 200):
        print ("Não foi possível obter o clima do local.")
        return None
    else:
        try:
            currentconditionresponse = json.loads(r.text)
            infoweather = {}
    #       print (pprint.pprint(currentconditionresponse))
            infoweather["weathersumary"] = currentconditionresponse[0]["WeatherText"]
            infoweather["temperature"] = currentconditionresponse[0]["Temperature"]["Metric"]["Value"]
            infoweather["localname"] = localname
            return infoweather
        except:
            return None

def pegarprevisao5dias(localcod):                      # Nesta função tem o código e o nome do local.
    dailyapiurl = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/" \
                             + localcod + "?apikey=" + acwapik + "&language=pt-br&metric=true"
    r = requests.get(dailyapiurl)
    if (r.status_code != 200):
        print ("Não foi possível obter o clima do local.")
        return None
    else:
        try:
            dailyresponse = json.loads(r.text)
            infoclima5dias = []
            for dia in dailyresponse['DailyForecasts']:
                climadia = {}
                climadia['maxima'] = dia ['Temperature']['Maximum']['Value']
                climadia['minima'] = dia ['Temperature']['Minimum']['Value']
                climadia['clima'] = dia ['Day']['IconPhrase']
                diasemana = int(date.fromtimestamp(dia['EpochDate']).strftime("%w"))
                climadia['dia'] = week[diasemana]
                infoclima5dias.append(climadia)
            return infoclima5dias
        except:
            return None

# http://dataservice.accuweather.com/forecasts/v1/daily/5day/2725728?apikey=NP3Amhm0ud2NrTtJLnuWTpHd2RthOOUH&language=pt-br&metric=true

# The program starts here
def showforecast(lat, long):
    try:
        mylocation = getlocalcod(lat, long)
        weathernow = getinfoweathernow(mylocation["localcod"], mylocation["localname"])
        print("Clima atual em: " + weathernow["localname"])
        print(weathernow["weathersumary"])
        print("Temperatura: " + str(
            weathernow["temperature"]) + "\xb0" + "C")  # A temperatura tem valor "float" então colocou-se
                                                        # o "str" para converter para "string"
    except:
        print('Erro ao obter o clima local.')

    option = input('\nDeseja saber a previsão dos próximos dias? (s ou n):').lower() #Interação com usuário para decidir se quer ou não a previsão do tempo para os próximos dias
    if option == 's':
        print("\nClima para hoje e para os próximos dias\n")

        try:
            previsao5dias = pegarprevisao5dias(mylocation["localcod"])
            #print(previsao5dias)
            for dia in previsao5dias:
                print(dia["dia"])
                print("Mínima: " + str(dia["minima"]) + "\xb0" + "C")
                print("Máxima: " + str(dia["maxima"]) + "\xb0" + "C")
                print("Clima: " + dia["clima"])
                print("--------------------------------")
            #print(previsao5dias)
        except:
            print('Erro ao obter a previsão para os próximos dias.')

def searchlocation (local):
    _local_ = urllib.parse.quote(local) #Uso de lib para coreção de codificação de espaços em url
    #print(_local_) #abaixo url do mapbox para geolocation substituição da apikey e do token por variáveis
    mapboxgeocode = "https://api.mapbox.com/geocoding/v5/mapbox.places/" \
                  + _local_ + ".json?access_token=" + mbtoken
    r = requests.get(mapboxgeocode)
    if (r.status_code != 200):
        print("Não foi possível obter o clima do local.")
        return None
    else:
        try:
            mapboxreponse = json.loads(r.text)
            coords2 = {}
            coords2['long'] = str (mapboxreponse['features'][0]['geometry']['coordinates'][0])
            coords2['lat'] = str (mapboxreponse['features'][0]['geometry']['coordinates'][1])
            #pprint.pprint (mapboxreponse)
            return coords2
        except:
            print('Erro na pesquisa do local.')

#The program start here
try:
    coordinates = getcoords()
    showforecast(coordinates["lat"], coordinates["long"]) #
    keepgoing = 's'

    while keepgoing == 's': #loop while para interação com usuário para ver previsão de outros locais no mundo
        keepgoing = input ('\nVocê gostaria de ver a previsão de outro local? (s ou n):').lower()
        if keepgoing != 's':
            break
        local = input('\nDigite a cidade e o estado: ')
        try:
            coords3 = searchlocation(local)
            showforecast(coords3['lat'], coords3['long'])
        except:
            print('Não foi possível obter a previsão para o local escolhido.')

except:
    print("Erro ao processar a solicitação. Entre em contato com o suporte.")
