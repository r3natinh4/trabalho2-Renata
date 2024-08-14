const fs = require("fs");
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function JSONCompare(item1, item2) {
    return item1.some((element) => {
        return JSON.stringify(item2) === JSON.stringify(element);
    });
}

class Account {
    constructor(name, phoneNumber, dateBirth, cep, password){
        this.name        = name.toLowerCase();
        this.phoneNumber = phoneNumber;
        this.dateBirth   = dateBirth.toLowerCase();
        this.cep         = cep;
        this.password    = password;
    }
    
    static register(name, phoneNumber, dateBirth, cep, password) {
        const file = fs.readFileSync("./db/accounts.json", "utf8");
        
        const data = JSON.parse(file);
        const dataInput = {
            name        : name.toLowerCase(),
            phoneNumber : phoneNumber,
            dateBirth   : dateBirth.toLowerCase(),
            cep         : cep,
            password    : password
        };
        
        if (JSONCompare(data, dataInput)) {
            return null;
        }
        
        data.push(dataInput);
        fs.writeFileSync("./db/accounts.json", JSON.stringify(data));
        return new Account(name, phoneNumber, dateBirth, cep, password);
    }
    
    static login(name, phoneNumber, dateBirth, cep, password) {
        const file = fs.readFileSync("./db/accounts.json", "utf8");
        
        const data = JSON.parse(file);
        const dataInput = {
            name        : name.toLowerCase(),
            phoneNumber : phoneNumber,
            dateBirth   : dateBirth.toLowerCase(),
            cep         : cep,
            password    : password
        };
        
        if (!JSONCompare(data, dataInput)) {
            return null;
        }
        
        return new Account(name, phoneNumber, dateBirth, cep, password);
    }
}

module.exports = Account;
