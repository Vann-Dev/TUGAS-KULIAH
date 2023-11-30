menuMakanan = [
    "bakso",
    "ayam bakar",
    "soto ayam",
    "nasi goreng"
]

menuDipilih = int(input("[Input] Mau pilih Makanan nomor berapa? \n"))

print(f"Anda memilih makananan nomor ke {menuDipilih} yaitu {menuMakanan[menuDipilih]}")

menuMakanan.insert(2, "pempek")

print(f"Menu makanan menjadi: {', '.join(menuMakanan)}")

menuDihapus = input("[Input] Tuliskan nama makanan yang mau di hapus dari menu? \n")

menuMakanan.remove(menuDihapus)

print(f"Menu makanan menjadi: {', '.join(menuMakanan)}")

menuMakanan.append("mie goreng")

print(f"Menu makanan menjadi: {', '.join(menuMakanan)}")
