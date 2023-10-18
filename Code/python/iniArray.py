array = [
    {
        "item": "buku",
        "harga": 5000,
        "id": "books",
        "tag": ["alat tulis", "mahal"]
    },
    {
        "item": "pensil",
        "harga": 2000,
        "id": "pencil",
        "tag": ["alat tulis", "murah"]
    },
    {
        "item": "penghapus",
        "harga": 1000,
        "id": "eraser",
        "tag": ["alat tulis", "murah"]
    },
    {
        "item": "penggaris",
        "harga": 5000,
        "id": "ruler",
        "tag": ["alat tulis", "mahal"]
    },
]

totalHarga = 0

for val in array:
    totalHarga = totalHarga + val["harga"]

print(f"Total harga barang: {totalHarga}")