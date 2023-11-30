print("============================ MATRIX ============================")
print()

kolomA = int(input("Masukkan jumlah kolom A: "))
barisA = int(input("Masukkan jumlah baris A: "))
kolomB = int(input("Masukkan jumlah kolom B: "))
barisB = int(input("Masukkan jumlah baris B: "))

matA = []
matB = []
matC = []

if kolomA == kolomB and barisA == barisB:
    print()
    print("============================ MATRIX A ============================")
    print()

    for b in range(barisA):
        toUse = []
        for k in range(kolomA):
            toUse.append(int(input(f"Masukkan matrix A[{b}][{k}]: ")))
        matA.append(toUse)

    print()
    print("============================ MATRIX B ============================")
    print()

    for b in range(barisB):
        toUse = []
        for k in range(kolomB):
            toUse.append(int(input(f"Masukkan matrix B[{b}][{k}]: ")))
        matB.append(toUse)

    print()
    print("============================ MATRIX C ============================")
    print()
            
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
    print()
    print("============================ ERROR ============================")
    print()

    print("Jumlah kolom dan baris A harus sama dengan jumlah kolom dan baris B")