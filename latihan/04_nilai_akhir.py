# Program Menghitung Nilai Akhir Mata Kuliah
tugas = float(input("Masukkan Nilai Tugas: "))
uts = float(input("Masukkan Nilai UTS: "))
uas = float(input("Masukkan Nilai UAS: "))

# Bobot nilai (contoh: Tugas 20%, UTS 30%, UAS 50%)
nilai_akhir = (tugas * 0.20) + (uts * 0.30) + (uas * 0.50)

print("\n=== HASIL NILAI AKHIR ===")
print("Nilai Akhir Mahasiswa:", nilai_akhir)