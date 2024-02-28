class Dokter:
    def __init__(self, id, nama, gaji):
        self.nama = nama
        self.id = id
        self.gaji = gaji

    def tunjangan(self, gaji):
        return gaji * 0.1
    
    def totalGaji(self, gaji):
        return self.tunjangan(gaji) + gaji
    
def main():
    namaDokter = input("Masukkan nama dokter: ")
    idDokter = input("Masukkan id dokter: ")
    gajiDokter = int(input("Masukkan gaji dokter: "))

    dokter = Dokter(None, None, None)
    dokter.id = idDokter
    dokter.nama = namaDokter
    dokter.gaji = gajiDokter

    print("Nama dokter: ", dokter.nama)
    print("Id dokter: ", dokter.id)
    print("Gaji dokter: ", dokter.gaji)
    print("Tunjangan: ", dokter.tunjangan(dokter.gaji))
    print("Total gaji: ", dokter.totalGaji(dokter.gaji))

main()
    