import os
import sys
import json

products = [
    {
        'name'        : 'Maçã',
        'price'       : 1.99,
        'description' : 'Vermelha/verde'
    },
    {
        'name'        : 'Manga',
        'price'       : 5.5,
        'description' : 'Rosa/espada'
    },
    {
        'name'        : 'Laranja',
        'price'       : 2.49,
        'description' : 'Lima/pera'
    },
    {
        'name'        : 'Banana',
        'price'       : 0.99,
        'description' : 'Prata/nanica'
    },
    {
        'name'        : 'Uva',
        'price'       : 2.9,
        'description' : 'Tompson/niagara'
    }
]

cart = []
history = []

class Account:
    def __init__(self, name, phone_number, date_birth, cep, password):
        self.name         = name.lower()
        self.phone_number = phone_number
        self.date_birth   = date_birth.lower()
        self.cep          = cep
        self.password     = password
    
    @classmethod
    def register(cls, name, phone_number, date_birth, cep, password):
        with open('db/accounts.json', 'r') as file:
            data = json.load(file)
            data_input = {
                'name'         : name.lower(),
                'phone_number' : phone_number,
                'date_birth'   : date_birth.lower(),
                'cep'          : cep,
                'password'     : password
            }
        
        if data_input in data:
            return None
        
        with open('db/accounts.json', 'w') as file:
            data.append(data_input)
            json.dump(data, file)
            return cls(name, phone_number, date_birth, cep, password)
    
    @classmethod
    def login(cls, name, phone_number, date_birth, cep, password):
        with open('db/accounts.json', 'r') as file:
            data = json.load(file)
            data_input = {
                'name'         : name.lower(),
                'phone_number' : phone_number,
                'date_birth'   : date_birth.lower(),
                'cep'          : cep,
                'password'     : password
            }
        
        if data_input not in data:
            return None
        
        return cls(name, phone_number, date_birth, cep, password)


def print_products():
    for index, product in enumerate(products):
        name = product['name']
        price = product['price']
        description = product['description']
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')

def add_to_cart(index):
    cart.append(products[index])

def show_cart():
    if len(cart) == 0:
        print('O carrinho está vazio.')
        return
    
    total = .0
    for index, product in enumerate(cart):
        name = product['name']
        price = product['price']
        description = product['description']
        total += price
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')
    
    print(f'\nPreço Total: R$ {total:.2f}')

def pay_products():
    if len(cart) == 0:
        print('Não há nenhum produto em seu carrinho para ser pago.')
        return
    
    total = .0
    for index, product in enumerate(cart):
        price = product['price']
        total += price
        
        history.append(product)
        del cart[index]  # "del product" não estava funcionando
    
    print('Compra feita com sucesso!\n' \
         f'Foi pago um total de R$ {total:.2f}')

def view_history():
    if len(history) == 0:
        print('Não foi feita nenhuma compra neste momento.')
        return
    
    total = .0
    for product in history:
        name = product['name']
        price = product['price']
        description = product['description']
        total += price
        
        print(f'{name}: R$ {price:.2f} - {description}')
    
    print(f'\nTotal Pago: R$ {total:.2f}')


def main():
    # Cria o arquivo caso ele não exista
    if not os.path.exists('db/accounts.json'):
        os.makedirs('db/', exist_ok=True)
        
        with open('db/accounts.json', 'a') as file:
            file.write('[]')
    
    print('Menu de Opções:')
    
    while True:
        print('\n1. Login\n' \
                '2. Registro\n' \
                '3. Sair\n')
        
        choice = input('O que você deseja fazer? ').strip()
        if choice not in ['1', '2', '3']:
            print('Escolha inválida.')
            continue
        
        if choice == '3':
            print('Até logo!')
            sys.exit()
        
        try:
            name = input('Digite seu nome: ').strip()
            phone_number = input('Digite seu número de telefone: ').strip()
            date_birth = input('Digite sua data de nascimento: ').strip()
            cep = input('Digite seu CEP: ').strip()
            password = input('Digite sua senha: ').strip()
        except AssertionError:
            continue
        
        if choice == '1':
            account = Account.login(name, phone_number, date_birth, cep, password)
        elif choice == '2':
                account = Account.register(name, phone_number, date_birth, cep, password)
        
        if account is None:
            print('Alguma coisa deu errado, tente novamente.')
            continue
        
        break
    
    print(f'Olá, {account.name}!')
    
    while True:
        print('\n1. Exibir Catálogo\n'          \
                '2. Adicionar ao carrinho\n'    \
                '3. Remover do carrinho\n'      \
                '4. Mostrar carrinho\n'         \
                '5. Pagar produtos\n'           \
                '6. Ver histórico de compras\n' \
                '7. Sair\n')
        
        choice = input('O que você deseja fazer? ').strip()
        if choice == '1':
            print('Catálogo de Frutas:\n')
            print_products()
        elif choice == '2':
            try:
                index = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                add_to_cart(index)
                print('O produto foi adicionado com sucesso ao carrinho.')
            except IndexError:
                print('Houve um erro ao adicionar o produto ao carrinho. O produto existe?')
            except ValueError:
                print('O código do produto não é um número inteiro.')
        elif choice == '3':
            try:
                index = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                del cart[index]
                print('O produto foi removido com sucesso do carrinho.')
            except IndexError:
                print('Houve um erro ao remover o produto do carrinho.')
            except ValueError:
                print('O código do produto não é um número inteiro.')
        elif choice == '4':
            print('Seu Carrinho:\n')
            show_cart()
        elif choice == '5':
            pay_products()
        elif choice == '6':
            view_history()
        elif choice == '7':
            print("\nAté logo!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()
