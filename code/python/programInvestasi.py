print(
"=======================================",
"Pehitungan Keuntungan saham:",
"======================================="
)

hargaAwal = int(input("Masukkan harga awal per saham (Rp): "))
hargaAkhir = int(input("Masukkan harga akhir per saham (Rp): "))
jumlahSaham = int(input("Masukkan jumlah saham: "))

totalKeuntungan = (hargaAkhir * jumlahSaham) - (hargaAwal * jumlahSaham)
persentaseKeuntungan = totalKeuntungan / (hargaAwal * jumlahSaham) * 100

print(
"----------------------------------------",
"Keuntungan setelah 1 tahun:",
"----------------------------------------"
)

print(f"Harga Awal per Saham\t: Rp. {hargaAwal}.00")
print(f"Harga Akhir per Saham\t: Rp. {hargaAkhir}.00")
print(f"Jumlah Saham\t\t: {jumlahSaham}")
print(f"Total Keuntungan\t: Rp. {totalKeuntungan}.00")
print(f"Persentase Keuntungan\t: {persentaseKeuntungan} %")