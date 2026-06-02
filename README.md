# Amazon GPU Tracker

Script Python que monitora preços de placas de vídeo na Amazon e salva o histórico em banco de dados local. Desenvolvido para automatizar o acompanhamento de preços sem depender de ferramentas externas.

---

## Como funciona

1. Faz uma requisição HTTP para a página de resultados da Amazon com headers de User-Agent para evitar bloqueio
2. Faz o parse do HTML com BeautifulSoup, extraindo nome, preço e link de cada produto
3. Limpa o valor monetário — remove `R$`, pontos e vírgulas — e converte para `float`
4. Filtra produtos sem título ou sem preço antes de salvar
5. Persiste os dados no banco SQLite via SQL puro com parâmetros preparados

---

## Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)

**Bibliotecas:** `requests` `beautifulsoup4` `sqlite3`

---

## Estrutura

```
amazon-gpu-tracker/
├── main.py        # ponto de entrada — coordena scraper e banco
├── screaper.py    # requisição HTTP, parse do HTML e extração dos dados
└── database.py    # criação da tabela, inserção e listagem via SQL puro
```

---

## Como rodar

```bash
# Clone o repositório
git clone https://github.com/viniciusroland01/amazon-gpu-tracker.git
cd amazon-gpu-tracker

# Instale as dependências
pip install requests beautifulsoup4

# Execute
python main.py
```

Os dados coletados são salvos em `produtos.db` na raiz do projeto.

---

## Observação

A Amazon bloqueia scraping com frequência. Caso a coleta retorne vazia, o User-Agent no `screaper.py` pode precisar ser atualizado com o do seu navegador atual.
