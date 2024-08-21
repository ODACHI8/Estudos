//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int dias = scanner.nextInt();
        int resto,meses,anos;

        anos = dias / 365;
        resto = dias % 365;
        meses = resto / 30;
        resto = resto % 30;
        dias = resto;
        System.out.printf("%d ano(s)\n%d mes(es)\n%d dia(s)\n",anos,meses,dias);

        scanner.close();
    }
}