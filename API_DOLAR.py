import requests

def dolar_API():
    response = requests.get('https://backend.selfspaces.com.br/cotacao-dia')
    data = response.json()
    dolar = data[0].get('valor_final')
    print(dolar)
    return dolar
