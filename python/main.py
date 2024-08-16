import os
import sys
from account import Account
import catalog

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
        
        match choice:
            case '1':
                account = Account.login(name, phone_number, date_birth, cep, password)
            case '2':
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
            catalog.print_products()
        elif choice == '2':
            try:
                index = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                catalog.add_to_cart(index)
                print('O produto foi adicionado com sucesso ao carrinho.')
            except IndexError:
                print('Houve um erro ao adicionar o produto ao carrinho. O produto existe?')
            except ValueError:
                print('O código do produto não é um número inteiro.')
        elif choice == '3':
            try:
                index = int(input('Qual produto você deseja adicionar ao carrinho? ').strip())
                catalog.remove_from_cart(index)
                print('O produto foi removido com sucesso do carrinho.')
            except IndexError:
                print('Houve um erro ao remover o produto do carrinho.')
            except ValueError:
                print('O código do produto não é um número inteiro.')
        elif choice == '4':
            print('Seu Carrinho:\n')
            catalog.show_cart()
        elif choice == '5':
            catalog.pay_products()
        elif choice == '6':
            catalog.view_history()
        elif choice == '7':
            print("\nAté logo!")
            break
        else:
            print("Opção inválida. Tente novamente!")

if __name__ == '__main__':
    main()
