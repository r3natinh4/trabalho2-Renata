const fs = require("fs");
const { ACCOUNTS_DB, Account } = require("./account.js");
const { PURCHASES_DB, printProducts, addToCart, removeFromCart, showCart, payProducts, viewPurchases } = require("./catalog.js");
const { validInput } = require("./handler.js");

const DIRECTORY_DB = "./db/";

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
