const fs = require("fs");
const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

const products = [
    {
        name        : "Maçã",
        price       : 1.99,
        description : "Vermelha/verde"
    },
    {
        name        : "Manga",
        price       : 5.5,
        description : "Rosa/espada"
    },
    {
        name        : "Laranja",
        price       : 2.49,
        description : "Lima/pera"
    },
    {
        name        : "Banana",
        price       : 0.99,
        description : "Prata/nanica"
    },
    {
        name        : "Uva",
        price       : 2.9,
        description : "Tompson/niagara"
    }
];

var cart    = [];
var history = [];
var account;


function validInput(text) {
    const output = new Promise((resolve) => {
        rl.question(text, (input) => {
            resolve(input.trim());
        });
    });
    
    return output;
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

function JSONCompare(item1, item2) {
    return item1.some((element) => {
        return JSON.stringify(item2) === JSON.stringify(element);
    });
}

function printProducts() {
    for (let index = 0; index < products.length; index++) {
        const product = products[index];
        
        let name        = product.name;
        let price       = product.price.toFixed(2);
        let description = product.description;
        
        console.log(`[${index}] ${name}: R$ ${price} - ${description}`);
    }
}

function addToCart(index) {
    cart.push(products[index]);
}

function removeFromCart(index) {
    cart.splice(index, 1);
}

function showCart() {
    if (cart.length === 0) {
        console.log("O carrinho está vazio.");
        return;
    }
    
    let total = 0.0;
    for (let index = 0; index < cart.length; index++) {
        let product = cart[index];
        
        let name        = product.name;
        let price       = product.price;
        let description = product.description;
        total += price;
        
        console.log(`[${index}] ${name}: R$ ${price.toFixed(2)} - ${description}`);
    }
    
    console.log(`\nPreço Total: R$ ${total.toFixed(2)}`);
}

function payProducts() {
    if (cart.length === 0) {
        console.log("Não há nenhum produto em seu carrinho para ser pago.");
        return;
    }
    
    let total = 0.0;
    for (let index = 0; index < cart.length; index++) {
        let product = cart[index];
        
        let price = product.price;
        total += price;
        
        history.push(product);
        removeFromCart(index);
    }
    
    console.log("Compra feita com sucesso!\n" +
                `Foi pago um total de R$ ${total.toFixed(2)}`);
}

function viewHistory() {
    if (history.length === 0) {
        console.log("Não foi feita nenhuma compra neste momento.");
        return;
    }
    
    let total = 0.0;
    history.forEach((product) => {
        let name        = product.name;
        let price       = product.price;
        let description = product.description;
        total += price;
        
        console.log(`${name}: R$ ${price.toFixed(2)} - ${description}`);
    });
    
    console.log(`\nTotal Pago: R$ ${total.toFixed(2)}`);
}


async function main() {
    if (!fs.existsSync("./db/accounts.json")) {
        fs.mkdirSync("./db/", { recursive: true });
        fs.writeFileSync("./db/accounts.json", "[]");
    }
    
    let loop = true;
    console.log("Menu de Opções:");
    
    while (loop) {
        console.log("\n1. Login\n"  +
                    "2. Registro\n" +
                    "3. Sair\n");
        
        let choice = await validInput("O que você deseja fazer? ");
        if (!["1", "2", "3"].includes(choice)) {
            console.log("Escolha inválida.");
            continue;
        }
        
        if (choice === "3") {
            console.log("Até logo!");
            process.exit();
        }
        
        let name;
        let phoneNumber;
        let dateBirth;
        let cep;
        let password;
        
        try {
            name        = await validInput("Digite seu nome: ");
            phoneNumber = await validInput("Digite seu número de telefone: ");
            dateBirth   = await validInput("Digite sua data de nascimento: ");
            cep         = await validInput("Digite seu CEP: ");
            password    = await validInput("Digite sua senha: ");
        } catch (e) {
            continue;
        }
        
        switch (choice) {
            case "1":
                account = Account.login(name, phoneNumber, dateBirth, cep, password);
                break;
            case "2":
                account = Account.register(name, phoneNumber, dateBirth, cep, password);
                break;
        }
        
        if (account === null) {
            console.log("Alguma coisa deu errado, tente novamente.");
            continue;
        }
        
        loop = false;
    }
    
    loop = true;
    console.log(`Olá, ${account.name}!`);
    
    while (loop) {
        console.log("\n1. Exibir Catálogo\n"          +
                      "2. Adicionar ao carrinho\n"    +
                      "3. Remover do carrinho\n"      +
                      "4. Mostrar carrinho\n"         +
                      "5. Pagar produtos\n"           +
                      "6. Ver histórico de compras\n" +
                      "7. Sair\n");
        
        let choice = await validInput("O que você deseja fazer? ");
        switch (choice) {
            case "1":
                console.log("Catálogo de Frutas:\n");
                printProducts();
                break;
            
            case "2":
                try {
                    let input = await validInput("Qual produto você deseja adicionar ao carrinho? ");
                    let index = parseInt(input);
                    addToCart(index);
                    console.log("O produto foi adicionado com sucesso ao carrinho.");
                } catch (e) {
                    console.log("Houve um erro ao adicionar o produto ao carrinho. O produto existe?");
                }
                break;
            
            case "3":
                try {
                    let input = await validInput("Qual produto você deseja adicionar ao carrinho? ");
                    let index = parseInt(input);
                    removeFromCart(index);
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
                payProducts();
                break;
            
            case "6":
                viewHistory();
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
