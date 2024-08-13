'combined_code.py'
class cadastro:
    def __init__(self, nome, númerodetelefone, datadenascimento, CEP): #iniciando uma classe
        self.nome = nome
        self.númerodetelefone = númerodetelefone
        self.datadenascimento = datadenascimento
        self.CEP = CEP
        
cadastros = []
#criamos um loop para adicionar cadastros

while 'true':
    resposta = input ("deseja adicionar cadastro? (s/n): ")
    if resposta.lower()!= '':


        #para ler as informações do cadastro
        arq = open("cadastro.txt","a")
        nome = input("Digite o nome: ")
        númerodetelefone = str(input("Digite seu número de telefone: "))
        datadenascimento = str(input("Digite a data de nascimento: "))
        CEP = str(input("Digite seu CEP: "))
        arq.write("{}, {}, {}, {}\n.format [nome, númerodetelefone, datadenascimento, CEP]")
        
        arq.close

        #criamos um dicionario para armazenar as informações do cadastro 
        cadastro_str = {"nome", "númerodetelefone", "datadenascimento", "CEP"}

        cadastro = str
        #para adicionar o cadastro ao vetor
        cadastros.append(cadastro)
        
        arquivo = open("clientes.txt", "a")
        
        print ("Cadastro adicionado com sucesso!")
    
    break
# Dicionário para armazenar as frutas
frutas = {
    "maçã": {"preco": 1.99, "descricao": "vermelha/verde"},
    "manga": {"preco": 5.50, "descricao": "rosa/espada"},
    "laranja": {"preco": 2.49, "descricao": "lima/pera"},
    "banana": {"preco": 0.99, "descricao": "prata/nanica"},
    "uva": {"preco": 2.90, "descricao": "tompson/niagara"}
}

# Função para exibir o catálogo de frutas
def exibir_catalogo():
    print("Catálogo de Frutas:")
    for fruta, detalhes in frutas.items():
        print(f"{fruta.capitalize()}: R$ {detalhes['preco']:.2f} - {detalhes['descricao'].capitalize()}")

# Função para adicionar uma fruta ao catálogo
def adicionar_fruta():
    nome = input("Digite o nome da fruta: ")
    preco = float(input("Digite o preço da fruta: "))
    descricao = input("Digite a descrição da fruta: ")
    frutas[nome.lower()] = {"preco": preco, "descricao": descricao}
    print("Fruta adicionada com sucesso!")

# Função para remover uma fruta do catálogo
def remover_fruta():
    nome = input("Digite o nome da fruta que deseja remover: ")
    if nome.lower() in frutas:
        del frutas[nome.lower()]
        print("Fruta removida com sucesso!")
    else:
        print("Fruta não encontrada!")

# Função principal
def main():
    while True:
        print("1. Exibir Catálogo")
        print("2. Adicionar Fruta")
        print("3. Remover Fruta")
        print("4. Sair")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            exibir_catalogo()
        elif opcao == "2":
            adicionar_fruta()
        elif opcao == "3":
            remover_fruta()
        elif opcao == "4":
            print("Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == "__main__":
    main()
