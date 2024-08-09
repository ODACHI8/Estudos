import java.util.Scanner;

public class Salario{
    //function que calcula o salario,hora*valor da hora.
    public static double valor(int horas, double valorPorHora){
        double resultado = horas * valorPorHora;
        return resultado;
    }
    public static void main(String[] args) {
        //Leitura das entradas.
        Scanner scanner = new Scanner(System.in);
        int Nfuncionario = scanner.nextInt();
        int Horas = scanner.nextInt();
        double Sal = scanner.nextDouble();

        //calculo do salario
        double finalsal = valor(Horas, Sal);

        //eximicao dos valores
        System.out.println("NUMBER = " + Nfuncionario);
        System.out.printf("SALARY = %.2f\n", finalsal);

        scanner.close();
    }
}