# Data Engineering Portfolio

Este projeto tem como objetivo demonstrar habilidades práticas em engenharia de dados através da construção de uma pipeline ETL modular. A solução inclui orquestração com Airflow, provisionamento de infraestrutura com Terraform e automação com CI/CD via GitHub Actions.

## 🧱 Estrutura do Projeto

- `src/`: Scripts de ingestão, transformação e carga de dados.
- `data/`: Dados em diferentes estágios (raw, staging, processed).
- `dags/`: Definição de DAGs do Airflow.
- `terraform/`: Arquivos de infraestrutura como código.
- `tests/`: Testes unitários dos scripts.
- `.github/workflows/`: Pipeline de automação com GitHub Actions.

## 🚀 Como executar localmente

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute os scripts diretamente (exemplo)
python src/ingestion/fetch_data.py
