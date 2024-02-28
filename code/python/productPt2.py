class Product:
    def __init__ (self):
        self.product_list = []

    def addProduct(self, name, price, quantity_available):
        self.product_list.append({
            'name': name, 
            'price': price, 
            'quantity': quantity_available
        })

    def totalProductsPrice(self):
        for product in self.product_list:
            print(f"Total harga produk {product['name']} adalah {product['price'] * product['quantity']}")

def main():
    product = Product()
    productsSize = int(input("Masukkan jumlah produk: "))

    currentProduct = 0
    while currentProduct < productsSize:
        productName = input("Masukkan nama produk: ")
        productPrice = int(input("Masukkan harga produk: "))
        productQuantity = int(input("Masukkan jumlah produk: "))

        product.addProduct(productName, productPrice, productQuantity)

        currentProduct += 1

    product.totalProductsPrice()

main()