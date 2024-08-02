const fs = require('fs');
const readline = require('readline');
const crypto = require('crypto');

const rl= readline.createInterface({
    input: process.stdin,
    output: process.stdout
});



function cadastrar(nome, idade, email, telefone) {
    const dados = `${nome};${idade};${email};${telefone}\n`;
    fs.appendFile('cadastros.txt', dados, (err) => {
      if (err) {
        console.error('Erro ao cadastrar:', err);
      } else {
        console.log('Cadastro realizado com sucesso!');
      }
    });
  }

  function login() {
    rl.question('digite email: ' , (resposta) => {
      email = resposta;
      rl.question('digite a senha ' , (resposta) => {
        senha = crypto.createHash('sha256').update(resposta).digest('hex');
        fs.readline('usuarios.txt', 'utf8', (err, data) => {
          if (err) {
        console.error('erro ao ler arquivo de usuarios', err);
          } else {
            const usuarios = data.split('\n');
            for (const usuario of usuarios) {
              const [nome, emailusuario, telefone, idade, senhausuario] = usuario.split(';');
              if (email === emailusuario && senha === senhausuario) {
                console.log ('login efetuado com sucesso');
                return;
              }
            }
            console.log ('email ou senha incorretos')
          }
        })
      })
    })
  }

  function listarCadastros() {
    fs.readFile('cadastros.txt', 'utf8', (err, data) => {
      if (err) {
        console.error('Erro ao ler arquivo:', err);
      } else {
        const cadastros = data.split('\n');
        cadastros.forEach((cadastro) => {
          const [nome, idade, email, telefone] = cadastro.split(';');
          console.log(`Nome: ${nome},Idade: ${idade}, E-mail: ${email}, Telefone: ${telefone}`);
        });
      }
    });
  }
  function menu() {
    console.log("Menu de Opções:");
    console.log("1. Login");
    console.log("2. Registro");
    console.log("3. Sair");
    rl.question("Escolha uma opção: ", (resposta) => {
      switch (resposta) {
        case "1":
          verificarLogin();
          break;
        case "2":
          cadastrarUsuario();
          break;
        case "3":
          process.exit();
        default:
          console.log("Opção inválida. Por favor, escolha novamente.");
          menu();
      }
    });
  }

  menu();
  function cadastrarUsuario() {
    rl.question('Digite o nome: ', (resposta) => {
      nome = resposta;
      rl.question('Digite o email: ', (resposta) => {
        email = resposta;
        rl.question('Digite o telefone: ', (resposta) => {
          telefone = resposta;
          rl.question('Digite a idade: ', (resposta) => {
            idade = resposta;
            rl.question('Digite a senha: ', (resposta) => {
              senha = crypto.createHash('sha256').update(resposta).digest('hex');
              const dados = `${nome};${email};${telefone};${idade};${senha}\n`;
              fs.appendFile('usuarios.txt', dados, (err) => {
                if (err) {
                  console.error('Erro ao criar usuário:', err);
                } else {
                  console.log('Usuário criado com sucesso!');
                  menu();
                }
              });
            });
          });
        });
      });
    });
  }

  function verificarLogin() {
    rl.question('Digite o email: ', (resposta) => {
      email = resposta;
      rl.question('Digite a senha: ', (resposta) => {
        senha = crypto.createHash('sha256').update(resposta).digest('hex');
        fs.readFile('usuarios.txt', 'utf8', (err, data) => {
          if (err) {
            console.error('Erro ao ler arquivo de usuários:', err);
          } else {
            const usuarios = data.split('\n');
            for (const usuario of usuarios) {
              const [nome, emailUsuario, telefone, idade, senhaUsuario] = usuario.split(';');
              if (email === emailUsuario && senha === senhaUsuario) {
                console.log('Login efetuado com sucesso!');
                menu();
                return;
              }
            }
            console.log('Email ou senha incorretos!');
            menu();
          }
        });
      });
    });
  }

  rl.question('Digite 1 para cadastrar ou 2 para listar cadastros: ', (resposta) => {
    if (resposta === '1') {
      rl.question('Digite o nome: ', (nome) => {
        rl.question('Digite a idade: ', (idade) => {
          rl.question('Digite o e-mail: ', (email) => {
            rl.question('Digite a senha: ', (senha) => {
              senha = crypto.createHash('sha256').update(resposta).digest('hex')
            rl.question('Digite o telefone: ', (telefone) => {
              cadastrar(nome, idade, email, senha, telefone);
              rl.close();
            });
          });
        });
      });
     });
    }
      else if (resposta === '2') {
          listarCadastros();
          rl.close();
      } else {
        console.log('Opção inválida!');
        rl.close();
      }
    });
