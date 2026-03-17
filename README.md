Este é um projeto de monitoramento de preços desenvolvido em Python

   **Tecnologias e Conceitos**
- **Python 3**: Linguagem principal.
- **Web Scraping**: Uso de `BeautifulSoup4` e `Requests` para extração de dados.
- **Banco de Dados**: Persistência de dados estruturada com **SQLite3**.

   **Estrutura do Projeto**
- `main.py`: Coordena a execução do scraper e salvamento.
- `screaper.py`: Contém a lógica de busca e limpeza de dados.
- `database.py`: Gerencia a criação da tabela e inserção no banco.

   Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install requests beautifulsoup4`
3. Execute: `python main.py`
