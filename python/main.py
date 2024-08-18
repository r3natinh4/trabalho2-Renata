import os
import sys
from account import ACCOUNTS_DB, Account
from catalog import PURCHASES_DB, print_products, add_to_cart, remove_from_cart, show_cart, pay_products, view_purchases

DIRECTORY_DB = './db/'

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
