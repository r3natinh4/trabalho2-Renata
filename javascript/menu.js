const readline = require('readline');

const catalogo = {
    "produto1": { "nome": "Produto 1", "preco": 10.99 },
    "produto2": { "nome": "Produto 2", "preco": 5.99 },
    "produto3": { "nome": "Produto 3", "preco": 7.99 },
    "produto4": { "nome": "Produto 4", "preco": 12.99 },
    "produto5": { "nome": "Produto 5", "preco": 8.99 }
};

let carrinho = {};

function adicionarProduto(produtoId) {
    if (catalogo.hasOwnProperty(produtoId)) {
        const produto = catalogo[produtoId];
        if (carrinho.hasOwnProperty(produtoId)) {
            carrinho[produtoId].quantidade += 1;
        } else {
            carrinho[produtoId] = { "nome": produto.nome, "preco": produto.preco, "quantidade": 1 };
        }
    } else {
        console.log("Produto não encontrado no catalogo.");
    }
}

function removerProduto(produtoId) {
    if (carrinho.hasOwnProperty(produtoId)) {
        delete carrinho[produtoId];
    } else {
        console.log("Produto não encontrado no carrinho.");
    }
}

function calcularTotal() {
    let total = 0;
    for (const produto in carrinho) {
        total += carrinho[produto].preco * carrinho[produto].quantidade;
    }
    return total;
}

function mostrarMenu() {
    console.log("Catalogo de produtos:");
    for (const produtoId in catalogo) {
        console.log(`${produtoId}: ${catalogo[produtoId].nome} - R$ ${catalogo[produtoId].preco.toFixed(2)}`);
    }
    console.log("\nCarrinho de compras:");
    for (const produtoId in carrinho) {
        console.log(`${produtoId}: ${carrinho[produtoId].nome} - R$ ${carrinho[produtoId].preco.toFixed(2)} x ${carrinho[produtoId].quantidade}`);
    }
    console.log(`\nTotal: R$ ${calcularTotal().toFixed(2)}`);
    console.log("\nOpções:");
    console.log("1. Adicionar produto ao carrinho");
    console.log("2. Remover produto do carrinho");
    console.log("3. Finalizar compra");
}

function lerOpcao() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    rl.question('Escolha uma opção: ', (opcao) => {
        if (opcao === "1") {
            rl.question('Digite o ID do produto: ', (produtoId) => {
                adicionarProduto(produtoId);
                rl.close();
                mostrarMenu();
            });
        } else if (opcao === "2") {
            rl.question('Digite o ID do produto: ', (produtoId) => {
                removerProduto(produtoId);
                rl.close();
                mostrarMenu();
            });
        } else if (opcao === "3") {
            console.log("Compra finalizada!");
            rl.close();
        } else {
            console.log("Opção inválida.");
            rl.close();
            mostrarMenu();
        }
    });
}

mostrarMenu();
lerOpcao();
