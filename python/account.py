from typing import Self
import json

class Account:
    def __init__(self, name, phone_number, date_birth, cep, password):
        self.name         = name.lower()
        self.phone_number = phone_number
        self.date_birth   = date_birth.lower()
        self.cep          = cep
        self.password     = password
    
    @classmethod
    def register(cls, name, phone_number, date_birth, cep, password):
        with open('db/accounts.json', 'r') as file:
            data = json.load(file)
            data_input = {
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
    def login(cls, name, phone_number, date_birth, cep, password):
        with open('db/accounts.json', 'r') as file:
            data = json.load(file)
            data_input = {
                'name'         : name.lower(),
                'phone_number' : phone_number,
                'date_birth'   : date_birth.lower(),
                'cep'          : cep,
                'password'     : password
            }
        
        if data_input not in data:
            return None
        
        return cls(name, phone_number, date_birth, cep, password)
