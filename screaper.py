#nome do produto
#preco do produto
#link do produto = https://www.amazon.com/s?k=placa+de+v%C3%ADdeo+5070ti&crid=8U6Z42DXL90U&sprefix=placa+de+v%C3%ADdeo+5070ti%2Caps%2C315&ref=nb_sb_noss
#elemento nome do produto = class="a-size-medium a-spacing-none a-color-base a-text-normal"
#elemento preco do produto = class="a-price-whole"
#a-link-normal = href="/ASUS-Graphics-Axial-tech-MaxContact-phase-change/dp/B0F8LGTHJD/ref=sr_1_1?crid=8U6Z42DXL90U&dib=eyJ2IjoiMSJ9.ATUy9GIsoY4m_mmzMD9xi8b5UcpjQgINqyHIK2o9GkCZX9DkMAD9D_GO7i7KWO5MgdjNfKF6OnwbYN05shTGC96hFmNzKkKaO6squyaAr2MQ6L9VR-q5dhD0Vr3cfXMV774ZsIDNX7EhyXFYRjmSZKNwQJZZdfvLw_KU8CIO9oRFQN9GUc7jS2Ran7-LRPqFy2_C0tJO_0sfmSUJc5BAFgVeZdLFR8X2KkHCNuuVjQ4.7feasYGLfDtC57kqTVg4m0iKMqtUQLP87L5-KuT5a20&dib_tag=se&keywords=placa+de+video+5070ti&qid=1773767580&sprefix=placa+de+v%C3%ADdeo+5070ti%2Caps%2C315&sr=8-1"
#userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36'

import requests
from bs4 import BeautifulSoup as bs

#funcao
def obter_produtos(url):
    cabecalhos = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
        "Accept-Language" : "pt-BR,pt;q=0.9"
    }
    resposta = requests.get(url , headers = cabecalhos)

    if resposta.status_code != 200:
        print('Erro ao acessar a página', resposta.status_code)
        return[]
    
    sopa = bs(resposta.text, "html.parser")

    produtos_html = sopa.find_all("div", {"data-component-type": "s-search-result"})

    lista_de_produtos = []

    for produto in produtos_html : 

        titulo_tag = produto.find("h2")
        titulo = titulo_tag.get_text(strip=True)if titulo_tag else "Sem título"
         
        preco_tag = produto.find("span", class_="a-price-whole")
        preco_texto = preco_tag.get_text(strip=True) if preco_tag else "0"

        try:
            limpeza = preco_texto.replace("R$","").replace("$","").replace(".","").replace(",","").strip()
            preco = float(limpeza)
        except ValueError:
            preco = 0.0

        link_tag = titulo_tag.find("a") if titulo_tag else None
        if not link_tag:
            link_tag = produto.find("a" , class_="a-link-normal")
        if link_tag and "href" in link_tag.attrs:
            href = link_tag['href']
            link = href if href.startswith("http") else "https://www.amazon.com" + href
        else:
            link = "Sem link"

        if titulo != "Sem título" and preco > 0:
            lista_de_produtos.append({
                "nome": titulo,
                "preco": preco,
                "link": link
            })

    return lista_de_produtos
    