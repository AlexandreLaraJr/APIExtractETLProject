import time
import requests
from datetime import datetime

def extractBitCoinValue():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json()
    return dados


def transformDataBitcoin(dados):
    value = dados['data']['amount']
    crypto_name = dados['data']['base']
    currency = dados['data']['currency']
    date = datetime.now()

    transformed_data = {
        'value': value,
        'crypto_name': crypto_name,
        'currency': currency,
        'date': date
    }
    
    return transformed_data

if __name__ == "__main__":
    while True:
        dados_json = extractBitCoinValue()
        dados_transformados = transformDataBitcoin(dados_json)
        print(dados_transformados)
        time.sleep(15)