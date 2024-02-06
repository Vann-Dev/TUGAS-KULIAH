import statistics

nilai = {
    "nama" : input("nama : "),
    "tugas1" : int(input("tugas 1 : " )),
    "tugas2" : int(input("tugas 2 : " )),
    "rata rata" : None
}

nilai["rata rata"] = statistics.mean([nilai["tugas1"], nilai["tugas2"]])

print(nilai)