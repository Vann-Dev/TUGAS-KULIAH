package segitiga;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            SegitigaHitung segitigaObj = new SegitigaHitung();

            System.out.print("Masukkan alas: ");
            segitigaObj.setAlas(input.nextInt());
            System.out.print("Masukkan tinggi: ");
            segitigaObj.setTinggi(input.nextInt());

            System.out.println("Luas segitiga: " + segitigaObj.luas());
            System.out.println("Keliling segitiga: " + segitigaObj.keliling());
        }
    }
}
