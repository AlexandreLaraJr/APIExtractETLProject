# Projeto ETL com Python e Requests

Este projeto implementa um pipeline ETL (Extração, Transformação, Carregamento) usando Python e a biblioteca `requests` para buscar dados de APIs externas.

## Visão Geral

Este pipeline ETL:

-   Extrai dados de várias APIs REST usando a biblioteca requests
-   Transforma os dados brutos em um formato estruturado
-   Carrega os dados processados em um destino final (ex: banco de dados, arquivos CSV)

## Requisitos

-   Python 3.8+
-   requests
-   pandas
-   python-dotenv

## Como Começar

1. Clone este repositório
2. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```
4. Crie um arquivo `.env` com suas credenciais da API:
    ```
    API_KEY=sua_chave_api
    API_SECRET=seu_segredo_api
    ```

## Uso

Execute o pipeline ETL:

```bash
python main.py
```

## Configuração

O pipeline ETL pode ser configurado usando o arquivo `config/config.yaml`. Modifique as configurações de acordo com suas necessidades:

-   Endpoints da API
-   Regras de transformação de dados
-   Destinos de saída

## Como Contribuir

1. Faça um fork do repositório
2. Crie uma nova branch
3. Faça suas alterações
4. Envie um pull request

## Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para detalhes.
