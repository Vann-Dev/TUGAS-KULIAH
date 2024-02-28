'''
Buatkan sebuah kelas Gudang yang memiliki atribut barnag untuk menyimpan inventaris barang
dengan jumlahnya. Terdapat method untuk menambahkan item ke inventaris, menghapus item
dari inventaris, dan menampilkan semua barang yang ada di inventaris. Program menggunakan
loop while untuk menampilkan menu kepada pengguna dan mengambil inputnya. Penggunaan
match-case / if -elif-else digunakan untuk memilih operasi yang sesuai dengan input pengguna.
'''

class Gudang:
    def __init__(self):
        self.inventaris = []

    def addItem(self, item):
        if self.inventaris.count(item) > 0:
            return False

        self.inventaris.append(item)

        return True

    def removeItem(self, item):        
        self.inventaris.pop(item - 1)
        return True

    def getItems(self):
        return self.inventaris
    
def main():
    gudang = Gudang()

    def printItems():
        print("No \t|\t Nama \t|\t Kuantiti")
        for i in range(len(gudang.getItems())):
            print(f"{i + 1} \t|\t {gudang.getItems()[i]['name']} \t|\t {gudang.getItems()[i]['quantity']}")

    loop =  True
    while loop:
        print(chr(27) + "[2J")
        printItems()
        print("\n\n")

        toDo = ""

        try:
            toDo = int(input("Masukkan apa yang ingin dilakukan:\n1. Tambah item ke inventaris\n2. Hapus item dari inventaris\n3. Keluar dari menu\n\n>  "))
        except:
            print("Tolong masukkan pilihan yang tepat.\n")
        
        match toDo:
            case 1:
                print(chr(27) + "[2J")
                name = input("Barang apa yang ingin dimasukkan? ")

                def addProduct():
                    try:
                        quantity = int(input("Masukkan quantity barang: "))
                        actions = gudang.addItem({
                            "name": name,
                            "quantity": quantity
                        })

                        if (actions == False):
                            print("Barang sudah ada di inventaris.")
                    except:
                        print("Tolong masukkan quantity yang benar.\n\n")
                        addProduct()

                addProduct()

            case 2:
                print(chr(27) + "[2J")
                def removeProduct():
                    printItems()
                    print("\n\n")

                    try:
                        itemToRemove = int(input("Pilih item yang ingin dihapus: "))

                        if len(gudang.getItems()) < itemToRemove:
                            print("Menu tidak ada\n\n")
                            return removeProduct()
                        
                        gudang.removeItem(itemToRemove)
                    except:
                        print("Harus berupa angka\n\n")
                        removeProduct()

                removeProduct()

            case 3:
                print("Aksi dibatalkan")
                loop = False

main()
