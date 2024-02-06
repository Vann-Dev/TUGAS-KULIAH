package segitiga;

public class SegitigaHitung {
    private int alas;
    private int tinggi;

    public void setAlas(int alas) {
        this.alas = alas;
    }

    public int getAlas() {
        return alas;
    }

    public void setTinggi(int tinggi) {
        this.tinggi = tinggi;
    }

    public int getTinggi() {
        return tinggi;
    }

    public int luas() {
        return alas * tinggi / 2;
    }

    public int keliling() {
        return alas * 3;
    }
}
