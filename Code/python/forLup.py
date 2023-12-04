print("============================ MATRIX ============================")
print()

kolomA = int(input("Masukkan jumlah kolom A: "))
barisA = int(input("Masukkan jumlah baris A: "))
kolomB = int(input("Masukkan jumlah kolom B: "))
barisB = int(input("Masukkan jumlah baris B: "))

matA = []
matB = []
matC = []

def makeMatrix(baris, kolom, matrix):
    for b in range(baris):
        column = []
        for k in range(kolom):
            column.append(int(input(f"Masukkan matrix [{b}][{k}]: ")))
        matrix.append(column)

def garis(isi):
    print()
    print(f"============================ {isi} ============================")
    print()

if kolomA == barisB and kolomB == barisA:
    garis("MATRIX A")

    makeMatrix(barisA, kolomA, matrix=matA)

    garis("MATRIX B")

    makeMatrix(barisB, kolomB, matrix=matB)

    garis("MATRIX C")

    for bb in range (barisA):
        kolom = []
        for kb in range(barisB):
            total = 0
            for ka in range(kolomA):
                total += matA[bb][ka] * matB[ka][kb]
            kolom.append(total)
        matC.append(kolom)

    for n in range(barisA):
        for k in range(kolomA):
            print(matC[n][k], end=" ")
        print()
        
else:
    garis("ERROR")

    print("Jumlah kolom dan baris A harus sama dengan jumlah kolom dan baris B")