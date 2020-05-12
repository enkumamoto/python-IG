# O módulo 'requests' realiza captura das requisições do http ou do https
import requests

# Abaixo, a linha diz para criar uma alias e que deve capturar requisições do domínio do google.
r = requests.get('https://www.google.com')

# Aqui no 'status_code' retorna o status das requisições, por exemplo quando retorno o número 200 significa 'ok' ou
# quando retorna 403 significa 'Forbidden' (informação protegida por senha) ou 404 que significa endereço errado.
print (r.status_code)

# Com '.headers' será apresentado o cabeçalho da requisição do http(s)
print (r.headers)

# Pode tratar (separar) as informações do cabeçalho usando '[]', por exemplo, foi pedido para verificar a data da
# requisição:
print (r.headers ['Date'])
print (r.headers ['Server'])
#print (r.headers ['Link'])
#print (r.headers ['Vary'])

# Com o '.text' será exibido o código html da página do google
print (r.text)