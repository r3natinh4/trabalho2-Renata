from random import randint
from parser import parse_txt

ACCOUNTS_DB = './db/accounts.txt'


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
        
        _name        = account['name']
        phone_number = account['phone_number']
        date_birth   = account['date_birth']
        cep          = account['cep']
        
        return cls(account_id, _name, phone_number, date_birth, cep)
    
    @classmethod
    def register(cls, name, phone_number, date_birth, cep, password):
        account_id = add_account(name, phone_number, date_birth, cep, password)
        
        if account_id is None:
            return None
        
        return cls(account_id, name, phone_number, date_birth, cep)
