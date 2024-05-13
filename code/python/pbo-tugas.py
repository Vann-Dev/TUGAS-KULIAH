import random

class Pengiriman:
    def __init__(self, pengirim, penerima, alamat, berat, harga, nomor_resi, jarak):
        self.pengirim = pengirim
        self.penerima = penerima
        self.alamat = alamat
        self.berat = berat
        self.harga = harga
        self.nomor_resi = nomor_resi
        self.jarak = jarak
        
        self.biaya_total = 0
        self.biaya_ongkir = 0

    def hitung_biaya(self):
        self.biaya_total = self.berat * self.harga

    def cetak(self):
        print("Pengirim:", self.pengirim)
        print("Penerima:", self.penerima)
        print("Alamat:", self.alamat)
        print("Berat:", self.berat)
        print("Harga:", self.harga)
        print("Nomor Resi:", self.nomor_resi)
        print("Biaya Total:", self.biaya_total)
    
    def diskon(self, diskon):
        self.biaya_total = self.biaya_total - (self.biaya_total * diskon)

    def hitung_biaya_ongkir(self):
        self.biaya_ongkir = self.jarak * 5000

    def perkirakan_waktu_pengiriman(self):
        waktu = self.jarak * 2
        print("Perkiraan waktu pengiriman:", waktu, "jam")


pengiriman = Pengiriman(
    pengirim=input("Masukkan nama pengirim: "),
    penerima=input("Masukkan nama penerima: "),
    alamat=input("Masukkan alamat penerima: "),
    berat=int(input("Masukkan berat barang: ")),
    harga=int(input("Masukkan harga barang: ")),
    nomor_resi=random.randint(100000, 999999),
    jarak=int(input("Masukkan jarak pengiriman: "))
)

print("\n\n")

pengiriman.hitung_biaya()
pengiriman.cetak()
pengiriman.diskon(0.1)
pengiriman.hitung_biaya_ongkir()
pengiriman.perkirakan_waktu_pengiriman()
print("Biaya Ongkir:", pengiriman.biaya_ongkir)
print("Biaya Total:", pengiriman.biaya_total + pengiriman.biaya_ongkir)