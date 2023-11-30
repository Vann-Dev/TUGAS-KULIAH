tinggi = float(input("Masukkan tinggi: \n=>\t"))
sisiA = float(input("Masukkan panjang sisi A: \n=>\t"))
sisiB = float(input("Masukkan panjang sisi B: \n=>\t"))

luas = 0.5 * (tinggi * (sisiA + sisiB))

print(f"Luas trapesium nya adalah: {luas} cm")


'''
PROGRAM Hitung_luas_trapesium

DEKLARASI:
    tinggi, sisiA, sisiB, luas : float

ALGORITMA:
    Read(sisiA, sisiB, tinggi)
    luas <- 0.5 * (tinggi * (sisiA + sisiB))
    Write(luas)
'''