gender = input("Masukkan gender: ")
tinggi = int(input("Masukkan tinggi: "))

if gender.lower() == "laki-laki":
    if tinggi < 166:
        print("Ga normal tinggi nya")
    else:
        print("Tinggi Normal")
elif gender.lower() == "perempuan":
    if tinggi < 154:
        print("Tinggi ga normal")
    else:
        print("Tinggi Normal")
else:
    print("We are sorry, we are not LGBTQA+ ABCDEFGHIJKLMNOPQRSTUVWXYZ")
