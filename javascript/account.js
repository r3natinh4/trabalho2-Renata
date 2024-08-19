const fs = require("fs");
const { randomInt } = require("crypto");
const { parseTXT } = require("./handler.js");

const ACCOUNTS_DB = "./db/accounts.txt";


function _getRandomId(limit = 999999999999) {
    const accounts = parseTXT(ACCOUNTS_DB);
    const usedIds = Object.keys(accounts);
    let generatedId;
    
    var loop = true;
    while (loop) {
        generatedId = String(randomInt(1, limit+1));
        
        if (!usedIds.includes(generatedId)) {
            loop = false;
        }
    }
    
    return generatedId;
}

function getAccount(name, password) {
    const accounts = parseTXT(ACCOUNTS_DB);
    var output = [ null, null ];
    
    for (const accountId in accounts) {
        const account = accounts[accountId];
        
        if (account.name.toLowerCase() === name.toLowerCase() &&
            account.password === password) {
            output[0] = accountId;
            output[1] = account;
            break;
        }
    }
    
    return output;
}

function addAccount(name, phoneNumber, dateBirth, cep, password) {
    const account = getAccount(name, password);
    
    if (account[0] !== null && account[1] !== null) {
        return null;
    }
    
    const generatedId = _getRandomId();
    
    fs.appendFileSync(ACCOUNTS_DB,
        `id           : ${generatedId}\n` +
        `name         : ${name}\n` +
        `phone_number : ${phoneNumber}\n` +
        `date_birth   : ${dateBirth}\n` +
        `cep          : ${cep}\n` +
        `password     : ${password}\n`);
    
    return generatedId;
}


class Account {
    constructor(id, name, phoneNumber, dateBirth, cep) {
        this.id          = id;
        this.name        = name;
        this.phoneNumber = phoneNumber;
        this.dateBirth   = dateBirth;
        this.cep         = cep;
        // this.password    = password;
    }
    
    static login(name, password) {
        const data = getAccount(name, password);
        
        const accountId = data[0]
        const account   = data[1]
        
        if (account === null) {
            return null;
        }
        
        const _name       = account.name
        const phoneNumber = account.phoneNumber;
        const dateBirth   = account.dateBirth;
        const cep         = account.cep;
        
        return new Account(accountId, _name, phoneNumber, dateBirth, cep);
    }
    
    static register(name, phoneNumber, dateBirth, cep, password) {
        const accountId = addAccount(name, phoneNumber, dateBirth, cep, password);
        
        if (accountId === null) {
            return null;
        }
        
        return new Account(accountId, name, phoneNumber, dateBirth, cep);
    }
}

module.exports = {
    ACCOUNTS_DB : ACCOUNTS_DB,
    Account     : Account
};
