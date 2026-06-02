# Amazon GPU Tracker

Script que monitora preços de GPUs na Amazon e salva o histórico em banco de dados local.

Faz a requisição com headers para evitar bloqueio, extrai nome, preço e link de cada produto, limpa o valor monetário para `float` e persiste tudo no SQLite via SQL puro.

---

## Stack

`Python` `BeautifulSoup` `Requests` `SQLite3`

---

## Como rodar

```bash
git clone https://github.com/viniciusroland01/amazon-gpu-tracker.git
cd amazon-gpu-tracker

pip install requests beautifulsoup4

python main.py
```

Os dados são salvos em `produtos.db` na raiz do projeto.
