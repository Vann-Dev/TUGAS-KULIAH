package dokter;

import java.util.Scanner;
import javax.swing.JOptionPane;

public class Main {
    public static void main(String[] args) {
        try (Scanner input = new Scanner(System.in)) {
            Dokter dokterObj = new Dokter();

            String idDokter = JOptionPane.showInputDialog("Masukkan id dokter: ");
            dokterObj.idDokter = idDokter;

            String namaDokter = JOptionPane.showInputDialog("Masukkan nama dokter: ");
            dokterObj.nama = namaDokter;

            String gajiDokter = JOptionPane.showInputDialog("Masukkan gaji dokter: ");
            dokterObj.gaji = Integer.parseInt(gajiDokter);

            System.out.println("ID Dokter: " + dokterObj.idDokter);
            System.out.println("Nama Dokter: " + dokterObj.nama);
            System.out.println("Gaji: " + dokterObj.gaji);
            System.out.println("Tunjangan: " + dokterObj.tunjangan());
            System.out.println("Total Gaji: " + dokterObj.totalGaji());
        }

    }
}
