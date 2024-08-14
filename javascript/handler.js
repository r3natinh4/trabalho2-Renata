const readline = require("readline");

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

function validInput(text) {
    const output = new Promise((resolve) => {
        rl.question(text, (input) => {
            resolve(input.trim());
        });
    });
    
    return output;
}

module.exports = {
    validInput : validInput
};
