class Sewa:
    def __init__(self, idPenyewa, nama, alamat, noKtp, jenisKendaraan, noPlat, lamaSewa, biayaSewa):
        self.idPenyewa = idPenyewa
        self.nama = nama
        self.alamat = alamat
        self.noKtp = noKtp
        self.jenisKendaraan = jenisKendaraan
        self.noPlat = noPlat
        self.lamaSewa = lamaSewa
        self.biayaSewa = biayaSewa

    def totalSewa(self):
        return self.lamaSewa * self.biayaSewa
    
    def potonganHarga(self):
        if self.lamaSewa >= 7:
            return 0.5 * self.totalSewa()
        
        if self.lamaSewa >= 5:
            return 0.3 * self.totalSewa()
        
        if self.lamaSewa >= 3:
            return 0.2 * self.totalSewa()
        
        if self.lamaSewa <= 2:
            return 0
        
    def ppn(self):
        return 0.2 * self.totalSewa()
    
    def jumlahBayar(self):
        return self.totalSewa() - self.potonganHarga() + self.ppn()
    
def main():
    idPenyewa = input("Masukkan id penyewa: ")
    nama = input("Masukkan nama: ")
    alamat = input("Masukkan alamat: ")
    noKtp = input("Masukkan no ktp: ")
    jenisKendaraan = input("Masukkan jenis kendaraan: ")
    noPlat = input("Masukkan no plat: ")
    lamaSewa = int(input("Masukkan lama sewa: "))
    biayaSewa = int(input("Masukkan biaya sewa: "))

    sewa = Sewa(idPenyewa, nama, alamat, noKtp, jenisKendaraan, noPlat, lamaSewa, biayaSewa)

    print(f"Total harga sewa: {sewa.totalSewa()}")
    print(f"Potongan harga: {sewa.potonganHarga()}")
    print(f"PPN: {sewa.ppn()}")
    print(f"Jumlah bayar: {sewa.jumlahBayar()}")

main()