class cadastro:
     def __init__(self, nome, número, datadenascimento, cep): #iniciando uma classe
       ' self.nome = nome'
       ' self.número = número'
       ' self.datadenascimento = data de nascimento'
       ' self.cep = cep'

cadastro = [] 
#loop para iniciar cadastro

while'true':
    resposta = input ("deseja adicionar um cadastro? (s/n): ")
    if resposta.lower()
       break

       #para ler as informações do cadastro 
       nome = input("Digite o nome: ")
       número = int(input("Digite o número: "))
       datadenascimento = int(input("Digite a data de nascimento: "))
       cep = int(input("Digite o cep: "))

#criamos um dicionario para armazenar as informações do cadastro
cadastro = {"nome", "número", "datadenascimento", "cep"}

#para adicionar o cadastro ao vetor
cadastro.append(cadastro)

print ("Cadastro adicionando com sucesso!")

#exibir o cadastro ja existente/adicionados
print("Cadastro:")
for cadastro in cadastros:
    print(cadastro)
