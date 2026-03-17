from screaper import obter_produtos
from database import criar_tabela , inserir_produto , listar_produtos

def main():
    url = "https://www.amazon.com/s?k=placa+de+v%C3%ADdeo+5070ti&crid=8U6Z42DXL90U&sprefix=placa+de+v%C3%ADdeo+5070ti%2Caps%2C315&ref=nb_sb_noss"

    criar_tabela()
    
    produtos = obter_produtos(url)

    for p in produtos:
        inserir_produto (p["nome"], p["preco"], p["link"])
         
    print("\n = = = Produtos no Banco = = = ")
    for produto in listar_produtos():
        print(produto)

if __name__ == "__main__" :
    main()