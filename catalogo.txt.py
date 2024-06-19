class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

class Catalogo:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                self.produtos.remove(produto)
                return
        print("Produto não encontrado!")

    def calcular_soma(self):
        soma = 0
        for produto in self.produtos:
            soma += produto.preco * produto.quantidade
        return soma

    def calcular_media(self):
        soma = self.calcular_soma()
        return soma / len(self.produtos)

    def aplicar_desconto(self, desconto):
        for produto in self.produtos:
            produto.preco *= (1 - desconto/100)

    def imprimir_catalogo(self):
        print("Catálogo:")
        for produto in self.produtos:
            print(f"  {produto.nome}: R$ {produto.preco:.2f} x {produto.quantidade} = R$ {(produto.preco * produto.quantidade):.2f}")

# Criar um catálogo
catalogo = Catalogo()

# Adicionar produtos ao catálogo
catalogo.adicionar_produto(Produto("Produto 1", 10.99, 2))
catalogo.adicionar_produto(Produto("Produto 2", 5.99, 3))
catalogo.adicionar_produto(Produto("Produto 3", 7.99, 1))

# Imprimir o catálogo
catalogo.imprimir_catalogo()

# Calcular a soma dos preços
print(f"Soma dos preços: R$ {catalogo.calcular_soma():.2f}")

# Calcular a média dos preços
print(f"Média dos preços: R$ {catalogo.calcular_media():.2f}")

# Aplicar um desconto de 10%
catalogo.aplicar_desconto(10)

# Imprimir o catálogo novamente
catalogo.imprimir_catalogo()
