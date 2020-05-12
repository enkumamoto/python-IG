# Este programa teve um "refactoring", todos os comentários estão em no arquivo "localizacao_do_usuario.py".
# Neste há novos comentários pertinentes ao processo de remodelação e organização do código.
# Nesta remodelação o programa apresentará a previsão para os próximos 5 dias e pegar a localização pelo ip do usuário.
import requests
import json
#import pprint
from datetime import date

acwapik = "MMw4pGhDAqUMWnZAnjtYZScGtflX7xSX"

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

try:
    coordinates = getcoords()
    mylocation = getlocalcod(coordinates["lat"], coordinates["long"])
    weathernow = getinfoweathernow(mylocation["localcod"], mylocation["localname"])
    print("Clima atual em: " + weathernow["localname"])
    print(weathernow["weathersumary"])
    print("Temperatura: " + str(weathernow["temperature"]) + "\xb0" + "C")  # A temperatura tem valor "float" então colocou-se
                                                                            # o "str" para converter para "string"
    print("\nClima para hoje e para os próximos dias\n")

    previsao5dias = pegarprevisao5dias(mylocation["localcod"])
    #print(previsao5dias)
    for dia in previsao5dias:
        print (dia["dia"])
        print ("Mínima: " + str(dia["minima"]) + "\xb0" + "C")
        print ("Máxima: " + str(dia["maxima"]) + "\xb0" + "C")
        print ("Clima: " + dia["clima"])
        print ("--------------------------------")
    #print(previsao5dias)

except:
    print("Erro ao processar a solicitação. Entre em contato com o suporte.")
