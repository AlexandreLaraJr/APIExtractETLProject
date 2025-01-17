import time
import requests
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

from database import Base, BitcoinPreco

# Carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

#cria o engine e sessão
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def createTable():
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso.")

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
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    
    return transformed_data

def saveDataPostgres(dados):
    session = Session()
    novo_registro = BitcoinPreco(**dados)
    session.add(novo_registro)
    session.commit()
    session.close()
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")

if __name__ == "__main__":
    createTable()
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extractBitCoinValue()
            if dados_json:
                dados_tratados = transformDataBitcoin(dados_json)
                print("Dados Tratados:", dados_tratados)
                saveDataPostgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)