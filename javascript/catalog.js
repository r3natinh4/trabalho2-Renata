const fs = require("fs");
const { parseTXT } = require("./handler.js");

const PURCHASES_DB = "./db/purchases.txt";

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

module.exports = {
    PURCHASES_DB   : PURCHASES_DB,
    printProducts  : printProducts,
    addToCart      : addToCart,
    removeFromCart : removeFromCart,
    showCart       : showCart,
    payProducts    : payProducts,
    viewPurchases  : viewPurchases
};
