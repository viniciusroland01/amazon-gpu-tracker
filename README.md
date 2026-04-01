# 🚀 Amazon GPU Tracker

Este é um projeto de **Web Scraping** desenvolvido em Python para monitorar preços de placas de vídeo (GPUs) na Amazon. A ferramenta automatiza a coleta de dados e garante a persistência das informações para futuras análises de mercado.

### 🎯 Objetivo do Projeto
Resolver o problema do monitoramento manual de preços, criando um histórico estruturado que permita identificar as melhores oportunidades de compra.

### 🛠️ Tecnologias e Conceitos
- **Python 3:** Linguagem base para toda a lógica de automação.
- **Web Scraping:** Extração de dados dinâmicos utilizando as bibliotecas **BeautifulSoup4** e **Requests**.
- **Banco de Dados:** Persistência de dados estruturada com **SQLite3** para armazenamento de histórico de preços.
- **Lógica de Limpeza de Dados:** Tratamento de strings e conversão de valores monetários para formatos numéricos processáveis.

### 📂 Estrutura do Projeto
- `main.py`: Ponto de entrada que coordena o fluxo de execução (Scraper -> Banco).
- `screaper.py`: Contém a lógica de requisição HTTP e o parse do HTML da Amazon.
- `database.py`: Gerencia a conexão, criação de tabelas e inserção de registros no banco de dados.

### ⚙️ Como Executar
1. Clone o repositório:
   ```bash
   git clone [https://github.com/viniciusroland01/amazon-gpu-tracker.git](https://github.com/viniciusroland01/amazon-gpu-tracker.git)
2. Instale as dependências : pip install requests beautifulsoup4
3. Execute python main.py
