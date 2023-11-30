kolomA = int(input("Masukkan jumlah kolom A "))
barisA = int(input("Masukkan jumlah baris A "))
kolomB = int(input("Masukkan jumlah kolom B "))
barisB = int(input("Masukkan jumlah baris B "))

matA = []
matB = []
matC = []

if kolomA == kolomB and barisA == barisB:
    for b in range(barisA):
        toUse = []
        for k in range(kolomA):
            toUse.append(int(input(f"Masukkan matrix A[{b}][{k}] ")))
        matA.append(toUse)

    for b in range(barisB):
        toUse = []
        for k in range(kolomB):
            toUse.append(int(input(f"Masukkan matrix B[{b}][{k}] ")))
        matB.append(toUse)
            
    for n in range(barisA):
        toUse = []
        for k in range(kolomA):
            toUse.append(matB[n][k] - matA[n][k])
        matC.append(toUse)

    for n in range(barisA):
        for k in range(kolomA):
            print(matC[n][k], end=" ")
        print()

else:
    print("Jumlah kolom dan baris A harus sama dengan jumlah kolom dan baris B")