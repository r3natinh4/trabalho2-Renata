import java.util.Scanner;

public class Cadastro {
    private String nome;
    private String numero;
    private String data de nascimento;
    private String cep;

    public Cadastro() {}

    public void cadastrar() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        nome = scanner.nextLine();

        System.out.print("Digite seu numero: ");
        email = scanner.nextLine();

        System.out.print("Digite sua data de nascimento: ");
        senha = scanner.nextLine();

        System.out.print("Digite seu cep: ");
        cpf = scanner.nextLine();

        System.out.println("Cadastro realizado com sucesso!");
        System.out.println("Dados cadastrados:");
        System.out.println("Nome: " + nome);
        System.out.println("numero: " + numero);
        System.out.println("data de nascimento: " + data de nascimento);
        System.out.println("cep: " + ce);
    }

    public static void main(String[] args) {
        Cadastro cadastro = new Cadastro();
        cadastro.cadastrar();
    }
}
