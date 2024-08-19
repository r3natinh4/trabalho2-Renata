import os
from parser import parse_txt

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


def _custom_price(price, dot=',', money='R$'):
    render = f'{price:.2f}'.replace('.', dot)
    return f'{money} {render}'


def print_products():
    for product_id in products:
        product = products[product_id]
        
        name        = product['name']
        price       = product['price']
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
