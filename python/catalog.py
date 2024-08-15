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

def print_products() -> None:
    for index, product in enumerate(products):
        name: str        = product['name']
        price: float     = product['price']
        description: str = product['description']
        
        print(f'[{index}] {name}: R$ {price:.2f} - {description}')

def add_to_cart(index: int) -> None:
    cart.append(products[index])

def remove_from_cart(index: int) -> None:
    del cart[index]

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
