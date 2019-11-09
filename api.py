import requests
import json

url = "https://restcountries.eu/rest/v2/all"
requisicao = requests.get(url)

paises = json.loads(requisicao.text) #parsing de json pra python

for pais in paises:
    print(pais['name'], pais['capital'])
