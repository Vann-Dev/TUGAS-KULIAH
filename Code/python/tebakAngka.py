import random
import os
angkaAcak = random.randrange(1, 6, 1)

tebakan = int(input("Tebak angka "))

if tebakan == angkaAcak:
    print("Baby")

os.remove(os.getcwd()+"/Code/python")
