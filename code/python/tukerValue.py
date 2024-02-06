a = 7
b = 5

print("Value awal: \na = {}\nb = {}".format(a, b))

'''
mengapa ini bisa?, karena code berjalan dalan 1 line, 
sehingga value tidak langsung berubah
'''
a, b = b, a 

print("Value akhir: \na = {}\nb = {}".format(a, b))