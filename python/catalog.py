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

def print_products():
    for index, product in enumerate(products):
        name = product['name']
        price = product['price']
        description = product['description']
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')

def add_to_cart(index):
    cart.append(products[index])

def remove_from_cart(index):
    del cart[index]

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
