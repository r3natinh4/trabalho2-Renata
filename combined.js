const fs = require("fs");
const { randomInt } = require("crypto");
const readline = require("readline");

const DIRECTORY_DB = "./db/";
const ACCOUNTS_DB  = "./db/accounts.txt";
const PURCHASES_DB = "./db/purchases.txt";

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const products = {
    1: {
        name        : "Maçã",
        price       : 1.99,
        description : "Vermelha/verde"
    },
    2: {
        name        : "Manga",
        price       : 5.5,
        description : "Rosa/espada"
    },
    3: {
        name        : "Laranja",
        price       : 2.49,
        description : "Lima/pera"
    },
    4: {
        name        : "Banana",
        price       : 0.99,
        description : "Prata/nanica"
    },
    5: {
        name        : "Uva",
        price       : 2.9,
        description : "Tompson/niagara"
    }
};

var cart = [];

function validInput(text) {
    const output = new Promise((resolve) => {
        rl.question(text, (input) => {
            resolve(input.trim());
        });
    });
    
    return output;
}

function parseTXT(filepath) {
    const data = {};
    var lastId = '-1';
    
    const file = fs.readFileSync(filepath, "utf8");
    const content = file.split("\n")
                        .map((line) => line.trim())
                        .filter((line) => line !== "");
    
    content.forEach((line) => {
        const match = line.match(/([a-zA-Z0-9_\-]+)(?:\s+)?(?::)(?:\s+)?(.+)/);
        
        if (match === null) {
            return;
        }
        
        const keyName  = match[1];
        const keyValue = match[2];
        
        if (keyName === "id") {
            lastId = keyValue;
            data[keyValue] = {};
        } else {
            data[lastId][keyName] = keyValue;
        }
    });
    
    return data;
}

function _customPrice(price, dot = ",", money = "R$") {
    const render = price.toFixed(2).replace('.', dot);
    return `${money} ${render}`;
}

function _productExists(productId) {
    const IDs = Object.keys(products);
    
    if (productId in IDs) {
        return true;
    }
    
    return false;
}


function printProducts() {
    for (const productId in products) {
        const product = products[productId];
        
        const name        = product.name;
        const price       = product.price;
        const description = product.description;
        
        console.log(`[${productId}] ${name}: ${_customPrice(price)} - ${description}`);
    }
}

function addToCart(index, quantity) {
    const productId = String(index);
    
    if (!_productExists(productId)) {
        throw new Error()
    }
    
    if (cart[productId] === undefined) {
        cart[productId] = 0;
    }
    
    cart[productId] += quantity;
}

function removeFromCart(index, quantity) {
    const productId = String(index);
    
    if (!_productExists(productId)) {
        throw new Error()
    }
    
    cart[productId] -= quantity;
    
    if (cart[productId] < 1) {
        delete cart[productId];
    }
}

function showCart() {
    if (cart.length === 0) {
        console.log("O carrinho está vazio.");
        return;
    }
    
    var total = 0.0;
    cart.forEach((quantity, productId) => {
        const product = products[productId];
        
        const name        = product.name;
        const price       = product.price * quantity;
        const description = product.description;
        
        total += price;
        console.log(`[${productId}] ${name} (${quantity}): ${_customPrice(price)} - ${description}`);
    });
    
    console.log(`\nPreço Total: ${_customPrice(total)}`);
}

function payProducts(accountId) {
    if (cart.length === 0) {
        console.log("Não há nenhum produto em seu carrinho para ser pago.");
        return;
    }
    
    const purchases = parseTXT(PURCHASES_DB);
    purchases[accountId] = purchases[accountId] ?? {};
    
    var total = 0.0;
    for (const productId in cart) {
        if (purchases[accountId][productId] === undefined) {
            purchases[accountId][productId] = 0;
        } else {
            purchases[accountId][productId] = parseInt(purchases[accountId][productId]);
        }
        
        purchases[accountId][productId] += parseInt(cart[productId]);
        total += products[productId].price * purchases[accountId][productId];
        
        delete cart[productId];
    }
    
    
    fs.unlinkSync(PURCHASES_DB);
    
    for (const userId in purchases) {
        fs.appendFileSync(PURCHASES_DB, `id : ${userId}\n`);
        
        for (const productId in purchases[userId]) {
            const quantity = purchases[userId][productId];
            fs.appendFileSync(PURCHASES_DB, `${productId} : ${quantity}\n`);
        }
    }
    
    
    console.log(
        "Compra feita com sucesso!\n" +
        `Foi pago um total de R$ ${_customPrice(total)}`);
}

function viewPurchases(accountId) {
    const purchases = parseTXT(PURCHASES_DB);
    const personal  = purchases[accountId] ?? {};
    
    if (personal.length === 0) {
        console.log("Não foi feita nenhuma compra nesta conta.");
        return;
    }
    
    var total = 0.0;
    for (const productId in personal) {
        const product  = products[productId];
        const quantity = parseInt(personal[productId]);
        
        const name        = product.name;
        const price       = product.price * quantity;
        const description = product.description;
        
        total += price;
        console.log(`[${productId}] ${name} (${quantity}): ${_customPrice(price)} - ${description}`);
    }
    
    console.log(`\nTotal Pago: ${_customPrice(total)}`);
}

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

async function main() {
    let account;
    let choice;
    
    if (!fs.existsSync(DIRECTORY_DB)) {
        fs.mkdirSync(DIRECTORY_DB, { recursive: true });
    }
    
    [ACCOUNTS_DB, PURCHASES_DB].forEach((dbPath) => {
        if (!fs.existsSync(dbPath)) {
            fs.writeFileSync(dbPath, "");
        }
    });
    
    let loop = true;
    console.log("Menu de Opções:");
    
    while (loop) {
        console.log(
            "\n1. Login\n"  +
            "2. Registro\n" +
            "3. Sair\n");
        
        choice = await validInput("O que você deseja fazer? ");
        
        let name;
        let phoneNumber;
        let dateBirth;
        let cep;
        let password;
        
        switch (choice) {
            case "1":
                name     = await validInput("Digite seu nome: ");
                password = await validInput("Digite sua senha: ");
                
                account = Account.login(name, password);
                break;
            case "2":
                name        = await validInput("Digite seu nome: ");
                phoneNumber = await validInput("Digite seu número de telefone: ");
                dateBirth   = await validInput("Digite sua data de nascimento: ");
                cep         = await validInput("Digite seu CEP: ");
                password    = await validInput("Digite sua senha: ");
                
                if ("" in []) {
                    console.log("Você esqueceu de preencher um ou mais campos. Tente novamente!");
                    continue;
                }
                
                account = Account.register(name, phoneNumber, dateBirth, cep, password);
                break;
            case "3":
                console.log("Até logo!");
                process.exit();
        }
        
        
        if (account === null) {
            console.log(
                "Alguma coisa deu errado, tente novamente.\n" +
                
                "\n    Coisas que podem ter acontecido:\n" +
                "No login, você preencheu as credenciais incorretamente ou a conta não existe.\n" +
                "No registro, já existe uma conta com o mesmo nome e senha.");
            
            continue;
        }
        
        loop = false;
    }
    
    loop = true;
    console.log(`Olá, ${account.name}!`);
    
    while (loop) {
        console.log(
            "\n1. Exibir Catálogo\n"        +
            "2. Adicionar ao carrinho\n"    +
            "3. Remover do carrinho\n"      +
            "4. Mostrar carrinho\n"         +
            "5. Pagar produtos\n"           +
            "6. Ver histórico de compras\n" +
            "7. Sair\n");
        
        choice = await validInput("O que você deseja fazer? ");
        
        let index;
        let quantity;
        
        switch (choice) {
            case "1":
                console.log("Catálogo de Frutas:\n");
                printProducts();
                break;
            
            case "2":
                try {
                    index    = parseInt(await validInput("Qual produto você deseja adicionar ao carrinho? "));
                    quantity = parseInt(await validInput("Quantos do mesmo produto você deseja adicionar? "));
                    
                    if (quantity < 1) {
                        console.log("Você não pode adicionar menos que 1 produto no carrinho.");
                        continue;
                    }
                    
                    addToCart(index, quantity);
                    
                    console.log("O produto foi adicionado com sucesso ao carrinho.");
                } catch (e) {
                    console.log("Houve um erro ao adicionar o produto ao carrinho. O produto existe?");
                }
                break;
            
            case "3":
                try {
                    index    = parseInt(await validInput("Qual produto você deseja remover do carrinho? "));
                    quantity = parseInt(await validInput("Quantos do mesmo produto você deseja remover? "));
                    
                    if (quantity < 1) {
                        console.log("Você não pode remover menos que 1 produto no carrinho.");
                        continue;
                    }
                    
                    removeFromCart(index, quantity);
                    
                    console.log("O produto foi removido com sucesso do carrinho.");
                } catch (e) {
                    console.log("Houve um erro ao remover o produto do carrinho.");
                }
                break;
            
            case "4":
                console.log("Seu Carrinho:\n");
                showCart();
                break;
            
            case "5":
                payProducts(account.id);
                break;
            
            case "6":
                viewPurchases(account.id);
                break;
            
            case "7":
                console.log("\nAté logo!");
                loop = false;
                break;
            
            default:
                console.log("Opção inválida. Tente novamente!");
                break;
        }
    }
    
    process.exit();
}

if (process.mainModule.filename === __filename) {
    main();
}
