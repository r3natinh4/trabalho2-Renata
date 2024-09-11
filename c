#include <stdio.h>

int main() {
    // Declaração de variáveis
    char nome[50];
    int idade;

    // Entrada de dados
    printf("Digite seu nome: ");
    scanf("%s", nome);
    printf("Digite sua idade: ");
    scanf("%d", &idade);

    // Saída de dados
    printf("\nOlá, eu sou %s! Tenho %d anos.\n", nome, idade);

    return 0;
}
