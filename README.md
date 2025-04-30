# Data Engineering Portfolio

Este projeto tem como objetivo demonstrar habilidades práticas em engenharia de dados através da construção de uma pipeline ETL modular.
A solução inclui orquestração com Airflow, provisionamento de infraestrutura com Terraform e automação com CI/CD via GitHub Actions.

## 🧱 Estrutura do Projeto

- `src/`: Scripts de ingestão, transformação e carga de dados.
- `data/`: Dados em diferentes estágios (raw, staging, processed).
- `dags/`: Definição de DAGs do Airflow.
- `terraform/`: Arquivos de infraestrutura como código.
- `tests/`: Testes unitários dos scripts.
- `.github/workflows/`: Pipeline de automação com GitHub Actions.

data-engineering-portfolio/  
├── data/ # Dados em diferentes estágios (raw, staging, processed)  
├── dags/ # DAGs do Apache Airflow  
├── src/ # Scripts de ingestão, transformação e carga  
├── terraform/ # Infraestrutura como código (IaC)  
├── tests/ # Testes unitários com Pytest  
├── .github/workflows/ # Pipeline CI com GitHub Actions  
├── requirements.txt # Dependências do projeto  
└── README.md  

## 🚀 Como executar localmente

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute os scripts diretamente (exemplo)
python src/ingestion/fetch_data.py

```

## ✅ Funcionalidades implementadas
* Ingestão de dados do Yahoo Finance

* Limpeza e padronização dos dados

* Cálculo de variação percentual diária

* Cálculo de médias móveis (MM7 e MM21)

* Detecção de quedas maiores que 5%

* Exportação dos dados processados por ação

* Testes unitários com Pytest

* Pipeline CI com cobertura de testes

## 🔧 Tecnologias Utilizadas
* Python

* Pandas

* yFinance

* Apache Airflow

* Terraform (simulado)

* GitHub Actions (CI)

* Pytest / Pytest-cov

## 📌 Próximos passos
* Upload dos arquivos para Amazon S3

* Orquestração do ETL com Airflow (a cada 2 dias)

* Construção de dashboard para visualização de indicadores

## 📄 Licença
* Distribuído sob a licença Apache 2.0. Veja LICENSE para mais informações.

## 🙋‍♂️ Contato
Desenvolvido por Wellington S. Santos.  
LinkedIn (www.linkedin.com/in/wellington-s-santos) • GitHub