#include <stdio.h>

void main()
{
    int quadrado[3][3];
    int resultado;
    
    printf("Defina os valores da matriz:\n");
    for(int i = 0; i<3 ; i++){
        for(int j = 0; j <3; j++) {
            printf("Valor [%d][%d]:\n",i,j);
            scanf("%d",&quadrado[i][j]);
        }
    }
    
    resultado = quadrado[1][0]+quadrado[2][0]+quadrado[2][1];
    
    printf("|%d, %d, %d|\n|%d, %d, %d|\n|%d, %d, %d|",quadrado[0][0],quadrado[0][1],quadrado[0][2],quadrado[1][0],quadrado[1][1],quadrado[1][2],quadrado[2][0],quadrado[2][1],quadrado[2][2]);
    printf("\n A soma dos valores abaixo da diagonal principal eh: %d !!!",resultado);
}