jarak = int(input("Masukkan jarak total: "))

km =  int(jarak / 100000)
m = int((jarak - (km * 100000)) / 100)
cm =  int(jarak - (km * 100000 + m * 100))


print(km + "dwadaw", m, cm)