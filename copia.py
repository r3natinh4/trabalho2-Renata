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

frutas_lista = """
-----------------
Lista de Frutas
-----------------
1. Maça - 7
2. Manga - 3
3. Laranja - 2
4. Banana - 4
5. Uva - 1
-----------------
"""
print(frutas_lista)
