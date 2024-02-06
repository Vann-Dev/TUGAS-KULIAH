print(
"=======================================",
"Program hitung harga barang setelah diskon:",
"======================================="
)

hargaBarang = int(input("Masukkan harga barang: "))
diskon = int(input("Diskon barang: "))

potonganHarga = hargaBarang * diskon / 100
hargaSetelahDiskon = hargaBarang - potonganHarga

print(
"----------------------------------------",
"Potongan harga:",
"----------------------------------------"
)

print(f"Potongan harga\t: Rp. {round(potonganHarga)}")
print(f"Harga setelah diskon\t: Rp. {round(hargaSetelahDiskon)}")