# Sistema de Monitoramento de Preços do Bitcoin

Este projeto consiste em uma solução completa para coleta, armazenamento e visualização de dados de preços do Bitcoin. O sistema é composto por uma pipeline ETL automatizada que coleta dados da Coinbase e um dashboard interativo para visualização das informações.

## Funcionalidades

### Pipeline ETL

-   Coleta automática de dados em tempo real da API Coinbase.
-   Transformação e processamento dos dados.
-   Armazenamento em banco de dados PostgreSQL.
-   Sistema de logging robusto.

### Dashboard

-   Visualização interativa dos preços do Bitcoin.
-   Gráficos de tendências e variações.
-   Atualização em tempo real.
-   Interface intuitiva construída com Streamlit.

## Pré-requisitos

-   Python 3.x
-   PostgreSQL
-   Pacotes Python necessários (instalar via `pip install -r requirements.txt`):
    -   requests
    -   sqlalchemy
    -   python-dotenv
    -   logfire
    -   psycopg2-binary
    -   streamlit
    -   pandas
    -   plotly

## Configuração do Ambiente

1. Clone o repositório:

```bash
git clone https://github.com/AlexandreLaraJr/APIExtractETLProject.git
cd APIExtractETLProject
```

2. Crie um arquivo `.env` no diretório raiz com as seguintes variáveis:

```
POSTGRES_USER=seu_usuario
POSTGRES_PASSWORD=sua_senha
POSTGRES_HOST=seu_host
POSTGRES_PORT=sua_porta
POSTGRES_DB=seu_banco
```

## Estrutura do Projeto

```
├── src/
│   ├── pipeline_03.py    # Script da pipeline ETL
│   ├── dashboard_01.py   # Aplicação do dashboard
│   └── database.py       # Configuração do banco de dados
├── .env                  # Variáveis de ambiente
├── requirements.txt      # Dependências do projeto
└── README.md
```

## Como Usar

### Executando a Pipeline ETL

Para iniciar a coleta de dados:

```bash
python src/pipeline_03.py
```

A pipeline irá:

-   Coletar dados da Coinbase a cada 15 segundos.
-   Processar e armazenar os dados no PostgreSQL.
-   Registrar todas as operações através do sistema de logging.

### Executando o Dashboard

Para iniciar a visualização dos dados:

```bash
streamlit run src/dashboard_01.py
```

O dashboard oferece:

-   Visualização em tempo real dos preços.
-   Gráficos interativos.
-   Análises estatísticas.
-   Filtros temporais.

## Monitoramento e Logging

O sistema utiliza Logfire para um monitoramento completo:

-   Registro de todas as operações da pipeline.
-   Monitoramento de performance.
-   Rastreamento de erros.
-   Métricas de execução.

## Tratamento de Erros

Implementamos tratamento robusto para diversos cenários:

-   Falhas de conexão com a API.
-   Problemas no banco de dados.
-   Erros de processamento.
-   Interrupções do sistema.

## Manutenção

### Pipeline

-   Verificar logs regularmente.
-   Monitorar uso do banco de dados.
-   Atualizar credenciais quando necessário.

### Dashboard

-   Verificar performance das consultas.
-   Atualizar visualizações conforme necessidade.
-   Monitorar uso de recursos.

## Autor

-   Alexandre Lara.

## Agradecimentos

-   Coinbase pela disponibilização da API.
-   Comunidade open source pelas ferramentas utilizadas.
-   Luciano Galvão Filho, pela aula do projeto.
