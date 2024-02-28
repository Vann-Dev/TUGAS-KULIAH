'''
Buatlah sebuah class bernama Restaurant yang memiliki atribut nama restoran, daftar menu
beserta harga, dan rating. Class ini harus memiliki method untuk menambahkan menu baru
beserta harganya, menghapus menu dari daftar, dan menampilkan daftar menu beserta harga
dan ratingnya. Program menggunakan loop while untuk menampilkan menu kepada pengguna
dan mengambil inputnya. Penggunaan match-case / if -elif-else digunakan untuk memilih
operasi yang sesuai dengan input pengguna. Menu program terdiri dari menambah menu baru,
menampilkan daftar menu, menghapus daftar menu.
'''

class Restaurant:
    def __init__(self, restaurantName):
        self.restaurantName = restaurantName
        self.menu = []

    def addItem(self, item):
        if self.menu.count(item) > 0:
            return False

        self.menu.append(item)

        return True

    def removeItem(self, item):        
        self.menu.pop(item - 1)
        return True

    def getItems(self):
        return self.menu
    
def main():
    restaurantName = input("Masukkan nama restoran: ")
    print("")

    restaurant = Restaurant(restaurantName)

    def printMenu():
        print(f"Daftar menu di {restaurant.restaurantName}")
        print("No \t|\t Nama \t|\t Harga \t|\t Rating")
        for i in range(len(restaurant.getItems())):
            print(f"{i + 1} \t|\t {restaurant.getItems()[i]['name']} \t|\t {restaurant.getItems()[i]['price']} \t|\t {restaurant.getItems()[i]['rate']}")
        print("\n\n")
        
    loop =  True
    while loop:
        print(chr(27) + "[2J")
        printMenu()
        toDo = ""

        try:
            toDo = int(input("Masukkan apa yang ingin dilakukan:\n1. Tambah makanan ke menu\n2. Hapus makanan dari menu\n3. Keluar dari menu\n\n>  "))
        except:
            print("Tolong masukkan pilihan yang tepat.\n")
        
        match toDo:
            case 1:
                print(chr(27) + "[2J")
                name = input("Nama makanan yang ingin dimasukkan: ")
                price = input("Masukkan harga makanan tersebut: ")

                def addMenu():
                    try:
                        rating = int(input("Masukkan rating dari 1 sampai 5: "))

                        if rating > 5 or rating < 0:
                            print("Masukkan rating dari 1 sampai 5\n\n")
                            return addMenu()
                        
                        actions = restaurant.addItem({
                            "name": name,
                            "price": price,
                            "rate": rating
                        })

                        if (actions == False):
                            print("Menu dengan data yang sama sudah ada")

                        print("")
                    except:
                        print("Masukkan rating dengan angka\n\n")
                        addMenu()

                addMenu()
                print("")

            case 2:              
                print(chr(27) + "[2J")  
                def menuRemove():
                    printMenu()

                    try:
                        itemToRemove = int(input("Nomor makanan apa yang ingin dihapus? "))
                        
                        if len(restaurant.getItems()) < itemToRemove:
                            print("Menu tidak ada\n\n")
                            return menuRemove()
                        
                        restaurant.removeItem(itemToRemove)
                    except:
                        print("Harus berupa angka\n\n")
                        menuRemove()

                menuRemove()
                print("")

            case 3:
                print("Aksi dibatalkan")
                loop = False

main()
