import requests

def buscar_dolar():
    response = requests.get('https://backend.selfspaces.com.br/cotacao-dia')
    dados = response.json()
    valor_dolar = dados[0].get('valor_final')
    print(valor_dolar)

buscar_dolar()