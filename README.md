# Cardápio Digital

Aplicação web para uma confeitaria feita em Django. O cliente navega pelo catálogo, monta o carrinho e finaliza o pedido pelo WhatsApp.

Tem sistema de cadastro e login com perfil do cliente, carrinho persistido por sessão e formatação de preços no padrão brasileiro.

---

## Stack

`Python` `Django` `SQLite` `HTML` `CSS`

---

## Como rodar

```bash
git clone https://github.com/viniciusroland01/cardapio-digital.git
cd cardapio-digital

python -m venv venv
venv\Scripts\activate

pip install django pillow

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Acesse `http://127.0.0.1:8000` para o cardápio e `/admin` para cadastrar produtos.

---

---

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
