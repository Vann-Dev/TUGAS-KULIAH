nim_mahasiswa = input("Masukkan NIM mahasiswa: ")
nama_mahasiswa = input("Masukkan nama mahasiswa: ")
nilai_tugas = int(input("Masukkan nilai tugas: "))
nilai_uts = int(input("Masukkan nilai uts: "))
nilai_uas = int(input("Masukkan nilai uas: "))

nilai_akhir = (0.3 * nilai_tugas) + (0.3 * nilai_uts) + (0.4 * nilai_uas)

print(f"nilai akhir mahasiswa yang bernama {nama_mahasiswa} dengan nim {nim_mahasiswa} memiliki total nilai {(123812831.3219312):.2f}")