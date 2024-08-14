import os
from account import Account
from catalog import print_products, add_to_cart, remove_from_cart, show_cart, pay_products, view_history

def valid_input(*args, **kwargs) -> str:
    for v in args:
        if v.strip() == '':
            raise Exception('placeholder')
    
    return input(*args, **kwargs).strip()

def main():
    # Cria o arquivo caso ele não exista
    if not os.path.exists('db/accounts.json'):
        os.makedirs('db/', exist_ok=True)
        
        with open('db/accounts.json', 'a') as file:
            file.write('[]')
    
    while True:
        choice: str = input('Você deseja se registrar ou logar? [r/l]: ').strip().lower()
        if choice not in ['r', 'l']:
            print('Escolha inválida.')
            continue
        
        try:
            name: str         = valid_input('Digite seu nome: ')
            phone_number: str = valid_input('Digite seu número de telefone: ')
            date_birth: str   = valid_input('Digite sua data de nascimento: ')
            cep: str          = valid_input('Digite seu CEP: ')
            password: str     = valid_input('Digite sua senha: ')
        except AssertionError:
            continue
        
        match choice:
            case 'r':
                account: Account = Account.register(name, phone_number, date_birth, cep, password)
            case 'l':
                account: Account = Account.login(name, phone_number, date_birth, cep, password)
        
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
                    index: int = int(input('Qual produto você deseja adicionar ao carrinho? '))
                    add_to_cart(index)
                    print('O produto foi adicionado com sucesso ao carrinho.')
                except IndexError:
                    print('Houve um erro ao adicionar o produto ao carrinho. O produto existe?')
            case '3':
                try:
                    index: int = int(input('Qual produto você deseja adicionar ao carrinho? '))
                    remove_from_cart(index)
                    print('O produto foi removido com sucesso do carrinho.')
                except IndexError:
                    print('Houve um erro ao remover o produto do carrinho.')
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
