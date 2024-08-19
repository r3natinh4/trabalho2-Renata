const fs = require("fs");
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

module.exports = {
    validInput : validInput,
    parseTXT   : parseTXT
};
