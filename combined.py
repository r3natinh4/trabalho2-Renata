import os
import sys
import json
from typing import Self

products: list[dict[str, str | float]] = [
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

cart: list[dict[str, str | float]] = []
history: list[dict[str, str | float]] = []

class Account:
    def __init__(self, name: str, phone_number: str, date_birth: str, cep: str, password: str) -> None:
        self.name         = name.lower()
        self.phone_number = phone_number
        self.date_birth   = date_birth.lower()
        self.cep          = cep
        self.password     = password
    
    @classmethod
    def register(cls, name: str, phone_number: str, date_birth: str, cep: str, password: str) -> Self | None:
        with open('db/accounts.json', 'r') as file:
            data: list[dict[str, str]] = json.load(file)
            data_input: dict[str, str] = {
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
    def login(cls, name: str, phone_number: str, date_birth: str, cep: str, password: str) -> Self | None:
        with open('db/accounts.json', 'r') as file:
            data: list[dict[str, str]] = json.load(file)
            data_input: dict[str, str] = {
                'name'         : name.lower(),
                'phone_number' : phone_number,
                'date_birth'   : date_birth.lower(),
                'cep'          : cep,
                'password'     : password
            }
        
        if data_input not in data:
            return None
        
        return cls(name, phone_number, date_birth, cep, password)


def print_products() -> None:
    for index, product in enumerate(products):
        name: str        = product['name']
        price: float     = product['price']
        description: str = product['description']
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')

def add_to_cart(index: int) -> None:
    cart.append(products[index])

def show_cart() -> None:
    if len(cart) == 0:
        print('O carrinho está vazio.')
        return
    
    total: float = .0
    for index, product in enumerate(cart):
        name: str        = product['name']
        price: float     = product['price']
        description: str = product['description']
        total += price
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')
    
    print(f'\nPreço Total: R$ {total:.2f}')

def pay_products() -> None:
    if len(cart) == 0:
        print('Não há nenhum produto em seu carrinho para ser pago.')
        return
    
    total: float = .0
    for index, product in enumerate(cart):
        price: float = product['price']
        total += price
        
        history.append(product)
        del cart[index]  # "del product" não estava funcionando
    
    print('Compra feita com sucesso!\n' \
         f'Foi pago um total de R$ {total:.2f}')

def view_history() -> None:
    if len(history) == 0:
        print('Não foi feita nenhuma compra neste momento.')
        return
    
    total: float = .0
    for product in history:
        name: str        = product['name']
        price: float     = product['price']
        description: str = product['description']
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
        
        choice: str = input('O que você deseja fazer? ').strip()
        if choice not in ['1', '2', '3']:
            print('Escolha inválida.')
            continue
        
        if choice == '3':
            print('Até logo!')
            sys.exit()
        
        try:
            name: str         = input('Digite seu nome: ').strip()
            phone_number: str = input('Digite seu número de telefone: ').strip()
            date_birth: str   = input('Digite sua data de nascimento: ').strip()
            cep: str          = input('Digite seu CEP: ').strip()
            password: str     = input('Digite sua senha: ').strip()
        except AssertionError:
            continue
        
        match choice:
            case '1':
                account: Account = Account.login(name, phone_number, date_birth, cep, password)
            case '2':
                account: Account = Account.register(name, phone_number, date_birth, cep, password)
        
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
        
        choice: str = input('O que você deseja fazer? ').strip()
        match choice:
            case '1':
                print('Catálogo de Frutas:\n')
                print_products()
            case '2':
                try:
                    index: int = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                    add_to_cart(index)
                    print('O produto foi adicionado com sucesso ao carrinho.')
                except IndexError:
                    print('Houve um erro ao adicionar o produto ao carrinho. O produto existe?')
                except ValueError:
                    print('O código do produto não é um número inteiro.')
            case '3':
                try:
                    index: int = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                    del cart[index]
                    print('O produto foi removido com sucesso do carrinho.')
                except IndexError:
                    print('Houve um erro ao remover o produto do carrinho.')
                except ValueError:
                    print('O código do produto não é um número inteiro.')
            case '4':
                print('Seu Carrinho:\n')
                show_cart()
            case '5':
                pay_products()
            case '6':
                view_history()
            case '7':
                print("\nAté logo!")
                break
            case _:
                print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()
