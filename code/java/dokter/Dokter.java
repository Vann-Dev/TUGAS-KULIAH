package dokter;

public class Dokter {
    public String idDokter;
    public String nama;
    public Integer gaji;

    public float tunjangan() {
        return gaji * 0.1f;
    }

    public float totalGaji() {
        return gaji + tunjangan();
    }
}
