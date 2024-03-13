package arrai;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            String nArray = JOptionPane.showInputDialog("Masukkan jumlah array: ");

            int n = Integer.parseInt(nArray);

            int[] arr = new int[n];

            for (int i = 0; i < n; i++) {
                String isi = JOptionPane.showInputDialog("Masukkan isi array ke-" + (i + 1) + ": ");
                arr[i] = Integer.parseInt(isi);
            }

            for (int i = 0; i < n; i++) {
                System.out.println("Isi array ke-" + (i + 1) + ": " + arr[i]);
            }
        }
    }
}
