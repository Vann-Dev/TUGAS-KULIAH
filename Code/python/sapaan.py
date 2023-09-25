import random
nama = input("Input nama: \n")
umur = int(input("Kamu umur brp: \n"))

class Orang:
    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur
        
    def bagiNoWa(self):
        if umur >= 18:
            print("Hai ganteng/cantik {} boleh kali bagi no wa".format(self.nama))
        else:
            print("Umur lu {}, kekecilan bro, maap yak".format(self.umur))
            
    def tanyaMtk(self):
        angka1 = random.randint(0, 100)
        angka2 = random.randint(0, 100)
        
        answer = int(input("Brp hasil {} dikali {}: \n".format(angka1, angka2)))
        
        if answer == (angka1 * angka2):
            print("Jawaban benar")
        else:
            print("Jawaban salah, hasilnya {}".format((angka1 * angka2)))

Orang(nama=nama, umur=umur).bagiNoWa()
Orang(nama=nama, umur=umur).tanyaMtk()
