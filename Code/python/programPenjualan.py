print(
"=================================================\n"
"PROGRAM HITUNG PENJUALAN LUKISAN\n"
"=================================================\n"
)

totalBarang = int(input("Masukkan berapa barang yang ingin di masukkan\t: "))

print("")

print(
"=================================================\n"
)

listBarang = []

for i in range(totalBarang):
    print(f"> Masukkan data barang ke {i + 1}\n")

    barang = {
        "kode transaksi": input("Kode transaksi\t:\t"),
        "nama barang": input("Nama barang\t:\t"),
        "ilustrator": input("Illustrator\t:\t"),
        "harga": int(input("Harga\t\t:\t")),
        "qty": int(input("Quantity\t:\t")),
        "subtotal": None,
        "ppn": 0.11,
        "total": None,
    }

    barang["subtotal"] = barang["harga"] * barang["qty"]

    barang["total"] =  round(barang["subtotal"] + barang["subtotal"] * barang["ppn"])

    listBarang.append(barang)

    print("\n")

print("\n")

print(
"-------------------------------------------------\n"
"HASIL\n"
"-------------------------------------------------\n"
)

print(listBarang)