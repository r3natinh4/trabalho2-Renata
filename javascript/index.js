const fs = require("fs");
const catalog = require("./catalog");
const Account = require("./account");
const { validInput } = require("./handler");

var account;

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
                catalog.printProducts();
                break;
            
            case "2":
                try {
                    let input = await validInput("Qual produto você deseja adicionar ao carrinho? ");
                    let index = parseInt(input);
                    catalog.addToCart(index);
                    console.log("O produto foi adicionado com sucesso ao carrinho.");
                } catch (e) {
                    console.log("Houve um erro ao adicionar o produto ao carrinho. O produto existe?");
                }
                break;
            
            case "3":
                try {
                    let input = await validInput("Qual produto você deseja remover do carrinho? ");
                    let index = parseInt(input);
                    catalog.removeFromCart(index);
                    console.log("O produto foi removido com sucesso do carrinho.");
                } catch (e) {
                    console.log("Houve um erro ao remover o produto do carrinho.");
                }
                break;
            
            case "4":
                console.log("Seu Carrinho:\n");
                catalog.showCart();
                break;
            
            case "5":
                catalog.payProducts();
                break;
            
            case "6":
                catalog.viewHistory();
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
