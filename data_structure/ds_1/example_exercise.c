
#include <stdio.h>
#include <string.h>



struct Livro {
  char titulo[100];
  char autor[100];
  int ano;
};



int main() {
  struct Livro meuLivro;


  printf("DIGITE O TITULO DO LIVRO: ");
  fgets(meuLivro.titulo, 100, stdin);
  meuLivro.titulo[strcspn(meuLivro.titulo, "\n")] = 0; // Remove a quebra de linha

   //leitura dos dados


  printf("AUTOR DO LIVRO: ");
  fgets(meuLivro.autor, 100, stdin);
  meuLivro.autor[strcspn(meuLivro.autor, "\n")] = 0;


  printf("ANO DO LIVRO: ");
  scanf("%d", &meuLivro.ano);


  printf("\n--- Informacoes do Livro ---\n");
  printf("TITULO: %s\n", meuLivro.titulo);
  printf("AUTOR: %s\n", meuLivro.autor);
  printf("ANO: %d\n", meuLivro.ano);
   //exibicao



  return 0;

}
