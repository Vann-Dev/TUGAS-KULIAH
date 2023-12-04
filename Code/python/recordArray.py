bil = []
i = 0
while True:
    print(f"Data ke {i+1}")
    data = {}
    data["x"] = float(input("X: "))
    data["y"] = float(input("Y: "))
    data["jml"] = round(data["x"] + data["y"], 2)
    print("Jumlah Data", data["jml"], end="\n\n")
    bil.append(data)
    stop = input("Input lagi? [y/n] ").upper()
    print()
    if (stop != "N"):
        i+=1
    else:
        break

print("no", "x", "y", "jumlah", sep="\t|", end="\n..............................................\n")
for i in range(len(bil)):
    print(i+1, bil[i]["x"], bil[i]["y"], bil[i]["jml"], sep="\t", end="\n")