class buah:
    def __init__(self):
        self.data = []
    
    def printBuah(self):
        print(self.data)

    def masukkanBuah(self, nama, warna, rasa):
        self.data.append({nama, warna, rasa})

Buah = buah() 
Buah.masukkanBuah("Apel", "Merah", "Manis")
Buah.masukkanBuah("Jeruk", "Orang", "Asam")
Buah.printBuah()

