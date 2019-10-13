#include <stdio.h>

int main(){
  char name[20];

  printf("What's your name: ");
    scanf("%s", name);
  printf("Greetings %s!", name);
  return 0;
}
