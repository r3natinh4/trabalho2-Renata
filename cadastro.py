
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
        nome = input("Digite o nome: ")
        númerodetelefone = str(input("Digite seu número de telefone: "))
        datadenascimento = str(input("Digite a data de nascimento: "))
        CEP = str(input("Digite seu CEP: "))

        #criamos um dicionario para armazenar as informações do cadastro 
        cadastro_str = {"nome", "númerodetelefone", "datadenascimento", "CEP"}

        #para adicionar o cadastro ao vetor
        cadastros.append(cadastro)
        
        arquivo = open("clientes.txt", "a")

        arquivo.write(cadastro_str)
        
        print ("Cadastro adicionado com sucesso!")
        
        break
