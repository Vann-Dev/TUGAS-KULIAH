bulan = int(input("Masukkan bulan: "))
tahun =  int(input("Masukkan Tahun: "))

jumlah_hari = 0

if bulan > 12 or bulan < 1:
    print("Invalid")
else:
    if bulan == (1 or 3 or 4 or 7 or 8 or 10 or 12):
        jumlah_hari =  31
    elif bulan == (4 or 6 or 9 or 11):
        jumlah_hari = 30
    
    if (bulan == 2):
        if (tahun % 4 == 0) and (tahun % 100 != 0) or (tahun % 400 == 0):
            jumlah_hari = 29
        else:
            jumlah_hari = 28

tipe_tahun = None

if jumlah_hari == 29:
    tipe_tahun = "Kabisat"
else:
    tipe_tahun = "Biasa"

print(f"Tahun: {tipe_tahun}")
print(f"Jumlah Hari: {jumlah_hari}")
