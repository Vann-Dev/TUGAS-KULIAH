print("Pilihan menu: \n 1. persegi \n 2. persegi panjang \n 3. lingkaran \n")

pilihan = int(input("Mau hitung apa kaka :D \t"))

if (pilihan == 1):
    panjang_sisi = float(input("Panjang sisi persegi ?\n"))
    luas_persegi = panjang_sisi ** 2
    keliling_persegi = 4 * panjang_sisi
    print("Luas persegi adalah {}".format(luas_persegi))
    print("Keliling persegi adalah {}".format(keliling_persegi))
    
elif (pilihan == 2):
    panjang = float(input("Panjang persegi panjang ?\n"))
    lebar = float(input("Lebar persegi panjang ?\n"))
    luas_persegi_panjang = panjang * lebar
    keliling_persegi_panjang = 2 * (panjang + lebar)
    print("Luas persegi panjang adalah {}".format(luas_persegi_panjang))
    print("Keliling persegi panjang adalah {}".format(keliling_persegi_panjang))
    
elif (pilihan == 3):
    jari_jari = float(input("Jari-jari lingkaran ?\n"))
    luas_lingkaran = 3.14 * jari_jari ** 2
    keliling_lingkaran = 2 * 3.14 * jari_jari
    print("Luas lingkaran adalah {}".format(luas_lingkaran))
    print("Keliling lingkaran adalah {}".format(keliling_lingkaran))
    
else:
    print("TIdak mendukung")