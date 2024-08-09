import java.util.Scanner;

public class Distancia{
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int tempo = scanner.nextInt();
        int distancia = tempo * 2;

        System.out.printf("%d minutos\n",distancia);
    }
}