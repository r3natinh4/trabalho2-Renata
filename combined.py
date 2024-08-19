import os
import sys
import re
from random import randint

DIRECTORY_DB = './db/'
ACCOUNTS_DB  = './db/accounts.txt'
PURCHASES_DB = './db/purchases.txt'

products = {
    '1': {
        'name'        : 'Maçã',
        'price'       : 1.99,
        'description' : 'Vermelha/verde'
    },
    '2': {
        'name'        : 'Manga',
        'price'       : 5.50,
        'description' : 'Rosa/espada'
    },
    '3': {
        'name'        : 'Laranja',
        'price'       : 2.49,
        'description' : 'Lima/pera'
    },
    '4': {
        'name'        : 'Banana',
        'price'       : 0.99,
        'description' : 'Prata/nanica'
    },
    '5': {
        'name'        : 'Uva',
        'price'       : 2.90,
        'description' : 'Tompson/niagara'
    }
}

cart = {}


def parse_txt(filepath):
    data = {}
    last_id  = '-1'
    
    with open(filepath, 'r') as file:
        content = [item.strip() for item in file.readlines() if item.strip() != '']
    
    for line in content:
        match = re.match(r'([a-zA-Z0-9_\-]+)(?:\s+)?(?::)(?:\s+)?(.+)', line)
        
        if match is None:
            continue
        
        key_name  = match.group(1)
        key_value = match.group(2)
        
        if key_name == 'id':
            last_id = key_value
            data[key_value] = {}
        else:
            data[last_id][key_name] = key_value
    
    return data


def _get_random_id(limit=999_999_999_999):
    accounts = parse_txt(ACCOUNTS_DB)
    used_ids = []
    generated_id = None
    
    for account_id in accounts:
        used_ids.append(account_id)
    
    while True:
        generated_id = str(randint(1, limit))
        
        if generated_id not in used_ids:
            break
    
    return generated_id

def get_account(name, password):
    accounts = parse_txt(ACCOUNTS_DB)
    
    for account_id in accounts:
        account = accounts[account_id]
        
        if account['name'].lower() == name.lower() and account['password'] == password:
            return account_id, account
    
    return None, None

def add_account(name, phone_number, date_birth, cep, password):
    if get_account(name, password) != (None, None):
        return None
    
    generated_id = _get_random_id()
    
    with open(ACCOUNTS_DB, 'a') as file:
        file.write(
            f'id           : {generated_id}\n'
            f'name         : {name}\n'
            f'phone_number : {phone_number}\n'
            f'date_birth   : {date_birth}\n'
            f'cep          : {cep}\n'
            f'password     : {password}\n'
        )
    
    return generated_id


class Account:
    def __init__(self, _id, name, phone_number, date_birth, cep):
        self.id           = _id
        self.name         = name
        self.phone_number = phone_number
        self.date_birth   = date_birth
        self.cep          = cep
        # self.password     = password
    
    @classmethod
    def login(cls, name, password):
        account_id, account = get_account(name, password)
        
        if account is None:
            return None
        
        name         = account['name']
        phone_number = account['phone_number']
        date_birth   = account['date_birth']
        cep          = account['cep']
        
        return cls(account_id, name, phone_number, date_birth, cep)
    
    @classmethod
    def register(cls, name, phone_number, date_birth, cep, password):
        account_id = add_account(name, phone_number, date_birth, cep, password)
        
        if account_id is None:
            return None
        
        return cls(account_id, name, phone_number, date_birth, cep)


def _custom_price(price, dot=',', money='R$'):
    render = f'{price:.2f}'.replace('.', dot)
    return f'{money} {render}'


def print_products():
    for product_id in products:
        product = products[product_id]
        
        name = product['name']
        price = product['price']
        description = product['description']
        
        print(f'[{product_id}] {name}: {_custom_price(price)} - {description}')

def add_to_cart(index, quantity):
    product_id = str(index)
    
    if cart.get(product_id) is None:
        cart[product_id] = 0
    
    cart[product_id] += quantity

def remove_from_cart(index, quantity):
    product_id = str(index)
    
    cart[product_id] -= quantity
    
    if cart[product_id] < 1:
        del cart[product_id]

def show_cart():
    if len(cart) == 0:
        print('O carrinho está vazio.')
        return
    
    total = .0
    for product_id in cart:
        product = products[product_id]
        
        quantity    = cart[product_id]
        name        = product['name']
        price       = product['price'] * quantity
        description = product['description']
        
        total += price
        print(f'[{product_id}] {name} ({quantity}): {_custom_price(price)} - {description}')
    
    print(f'\nPreço Total: {_custom_price(total)}')

def pay_products(account_id):
    if len(cart) == 0:
        print('Não há nenhum produto em seu carrinho para ser pago.')
        return
    
    purchases = parse_txt(PURCHASES_DB)
    purchases[account_id] = purchases.get(account_id, {})
    
    total = .0
    for product_id in list(cart):
        if purchases[account_id].get(product_id) is None:
            purchases[account_id][product_id] = 0
        else:
            purchases[account_id][product_id] = int(purchases[account_id][product_id])
        
        purchases[account_id][product_id] += int(cart[product_id])
        
        total += products[product_id]['price'] * purchases[account_id][product_id]
        
        del cart[product_id]
    
    
    os.remove(PURCHASES_DB)
    
    with open(PURCHASES_DB, 'a') as file:
        for user_id in purchases:
            file.write(f'id : {user_id}\n')
            
            for product_id in purchases[user_id]:
                quantity = purchases[user_id][product_id]
                file.write(f'{product_id} : {quantity}\n')
    
    
    print(
        'Compra feita com sucesso!\n'
       f'Foi pago um total de {_custom_price(total)}')

def view_purchases(account_id):
    purchases = parse_txt(PURCHASES_DB)
    personal  = purchases.get(account_id, {})
    
    if len(personal) == 0:
        print('Não foi feita nenhuma compra nesta conta.')
        return
    
    total = .0
    for product_id in personal:
        product  = products[product_id]
        quantity = int(personal[product_id])
        
        name        = product['name']
        price       = product['price'] * quantity
        description = product['description']
        
        total += price
        print(f'[{product_id}] {name} ({quantity}): {_custom_price(price)} - {description}')
    
    print(f'\nTotal Pago: {_custom_price(total)}')


def main():
    # Cria os arquivos caso eles não existam
    for db_path in (ACCOUNTS_DB, PURCHASES_DB):
        if not os.path.exists(db_path):
            os.makedirs(DIRECTORY_DB, exist_ok=True)
            
            with open(db_path, 'w') as file:
                file.write('')
    
    
    print('Menu de Opções:')
    
    while True:
        print(
            '\n1. Login\n'
            '2. Registro\n'
            '3. Sair\n')
        
        choice = input('O que você deseja fazer? ').strip()
        
        if choice == '1':
            name     = input('Digite seu nome: ').strip()
            password = input('Digite sua senha: ').strip()
            
            account = Account.login(name, password)
        elif choice == '2':
            name         = input('Digite seu nome: ').strip()
            phone_number = input('Digite seu número de telefone: ').strip()
            date_birth   = input('Digite sua data de nascimento: ').strip()
            cep          = input('Digite seu CEP: ').strip()
            password     = input('Digite sua senha: ').strip()
            
            if '' in (name, phone_number, date_birth, cep, password):
                print('Você esqueceu de preencher um ou mais campos. Tente novamente!')
                continue
            
            account = Account.register(name, phone_number, date_birth, cep, password)
        elif choice == '3':
            print('Até logo!')
            sys.exit()
        else:
            print('Escolha inválida.')
            continue
        
        
        if account is None:
            print(
                'Alguma coisa deu errado, tente novamente.\n'
                
                '\n    Coisas que podem ter acontecido:\n'
                'No login, você preencheu as credenciais incorretamente ou a conta não existe.\n'
                'No registro, já existe uma conta com o mesmo nome e senha.')
            
            continue
        
        break
    
    
    print(f'Olá, {account.name}!')
    
    while True:
        print(
            '\n1. Exibir Catálogo\n'          
            '2. Adicionar ao carrinho\n'
            '3. Remover do carrinho\n'
            '4. Mostrar carrinho\n'
            '5. Pagar produtos\n'
            '6. Ver histórico de compras\n'
            '7. Sair\n')
        
        choice = input('O que você deseja fazer? ').strip()
        if choice == '1':
            print('Catálogo de Frutas:\n')
            print_products()
        
        elif choice == '2':
            try:
                index = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                quantity = int(input('Quantos do mesmo produto você deseja adicionar? ').strip())
                
                if quantity < 1:
                    print('Você não pode adicionar menos que 1 produto no carrinho.')
                    continue
                
                add_to_cart(index, quantity)
                
                print('O produto foi adicionado com sucesso ao carrinho.')
            except IndexError:
                print('Houve um erro ao adicionar o produto ao carrinho. O produto existe?')
            except ValueError:
                print('O código do produto ou a quantidade não é um número.')
        
        elif choice == '3':
            try:
                index = int(input('Qual produto você deseja remover do carrinho? ').strip())
                quantity = int(input('Quantos do mesmo produto você deseja remover? ').strip())
                
                if quantity < 1:
                    print('Você não pode remover menos que 1 produto no carrinho.')
                    continue
                
                remove_from_cart(index, quantity)
                
                print('O produto foi removido com sucesso do carrinho.')
            except IndexError:
                print('Houve um erro ao remover o produto do carrinho. O produto não está no carrinho?')
            except ValueError:
                print('O código do produto ou a quantidade não é um número.')
        
        elif choice == '4':
            print('Seu Carrinho:\n')
            show_cart()
        
        elif choice == '5':
            pay_products(account.id)
        
        elif choice == '6':
            view_purchases(account.id)
        
        elif choice == '7':
            print("\nAté logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()
