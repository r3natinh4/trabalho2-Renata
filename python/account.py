import re
from random import randint

ACCOUNTS_DB  = './db/accounts.txt'


def _get_accounts():
    accounts = {}
    last_id  = '-1'
    
    with open(ACCOUNTS_DB, 'r') as file:
        content = [item.strip() for item in file.readlines() if item.strip() != '']
    
    for line in content:
        match = re.match(r'([a-zA-Z0-9]+)(?:\s+)?(?::)(?:\s+)?(.+)', line)
        
        if match is None:
            continue
        
        key_name  = match.group(1)
        key_value = match.group(2)
        
        if key_name == 'id':
            last_id = key_value
            accounts[key_value] = {}
        else:
            accounts[last_id][key_name] = key_value
    
    return accounts

def _get_random_id(limit=999_999_999_999):
    accounts = _get_accounts()
    generated_id = None
    loop = True
    
    while loop:
        generated_id = str(randint(1, limit))
        
        for account_id in accounts:
            account = accounts[account_id]
            
            if generated_id != account['id']:
                loop = False
    
    return generated_id

def get_account(name, password):
    accounts = _get_accounts()
    
    for account_id in accounts:
        account = accounts[account_id]
        
        if account['name'].lower() == name.lower() and account['password'] == password:
            return account_id
    
    return None

def add_account(name, date_birth, cep, email, password):
    generated_id = _get_random_id()
    
    with open(ACCOUNTS_DB, 'a') as file:
        file.write(
            f'id         : {generated_id}\n'
            f'name       : {name}\n'
            f'date_birth : {date_birth}\n'
            f'cep        : {cep}\n'
            f'email      : {email}\n'
            f'password   : {password}\n'
        )
    
    return generated_id, {
        'name'       : name,
        'date_birth' : date_birth,
        'cep'        : cep,
        'email'      : email
    }


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
        return cls(account_id, name, phone_number, date_birth, cep)
