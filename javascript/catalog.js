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

module.exports = {
    printProducts  : printProducts,
    addToCart      : addToCart,
    removeFromCart : removeFromCart,
    showCart       : showCart,
    payProducts    : payProducts,
    viewHistory    : viewHistory
};
