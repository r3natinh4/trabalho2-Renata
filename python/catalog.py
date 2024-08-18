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

cart      = {}
purchases = {}


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
        cart[product_id] = { 'quantity': 0 }
    
    cart[product_id]['quantity'] += quantity

def remove_from_cart(index, quantity):
    product_id = str(index)
    
    cart[product_id]['quantity'] -= quantity
    
    if cart[product_id]['quantity'] < 1:
        del cart[product_id]

def show_cart():
    if len(cart) == 0:
        print('O carrinho está vazio.')
        return
    
    total = .0
    for product_id in cart:
        product = products[product_id]
        
        quantity    = cart[product_id]['quantity']
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
    
    purchases_data = parse_txt(PURCHASES_DB)
    if purchases_data.get(account_id) is None:
        purchases_data[account_id] = {}
    
    personal_data  = purchases_data[account_id]
    del purchases_data[account_id]
    
    total = .0
    for product_id in cart:
        product  = products[product_id]
        cproduct = cart[product_id]
        
        quantity = cproduct['quantity']
        price    = product['price'] * quantity
        total   += price
        
        if purchases.get(product_id) is None:
            purchases[product_id] = { 'quantity': 0 }
        
        purchases[product_id]['quantity'] += quantity
    
    os.remove(PURCHASES_DB)
    with open(PURCHASES_DB, 'a') as file:
        file.write(f'id : {account_id}\n')
        for purchase_id in list(purchases_data):
            quantity = purchases.get(purchase_id, { 'quantity': 0 })['quantity'] \
                     + int(personal_data.get(purchase_id, 0))
            
            file.write(f'{purchase_id} : {quantity}\n')
            
            del cart[product_id]
            del purchases[purchase_id]
        
        for data in purchases_data:
            file.write(f'{data} : {purchases_data[data]}\n')
    
    print(
        'Compra feita com sucesso!\n'
       f'Foi pago um total de {_custom_price(total)}')

def view_purchases(account_id):
    purchases_data = parse_txt(PURCHASES_DB)
    personal_data  = purchases_data.get(account_id, {})
    
    if len(personal_data) == 0:
        print('Não foi feita nenhuma compra nesta conta.')
        return
    
    total = .0
    for product_id in personal_data:
        product  = personal_data[product_id]
        pproduct = products[product_id]
        
        quantity    = product['quantity']
        name        = pproduct['name']
        price       = pproduct['price'] * quantity
        description = pproduct['description']
        
        total += price
        print(f'[{product_id}] {name} ({quantity}): {_custom_price(price)} - {description}')
    
    print(f'\nTotal Pago: {_custom_price(total)}')
