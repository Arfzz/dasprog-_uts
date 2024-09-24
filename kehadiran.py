# Meminta input nilai ujian dan kehadiran dari user
nilai_ujian = float(input("Masukkan nilai ujian: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

# Cek jika kehadiran kurang dari 50%
if kehadiran < 50:
    print("Tidak lulus karena kehadiran kurang dari 50%")
else:
    # Cek jika nilai ujian kurang dari 70
    if nilai_ujian < 70:
        print(f"Nilai ujian adalah {nilai_ujian}, dan tidak dihitung rata-rata karena kurang dari 70.")
    else:
        # Jika kehadiran mencukupi dan nilai ujian lebih dari atau sama dengan 70
        tugas = float(input("Masukkan nilai tugas: "))
        proyek = float(input("Masukkan nilai proyek: "))
        
        # Hitung rata-rata dari nilai ujian, tugas, dan proyek
        rata_rata = (nilai_ujian + tugas + proyek) / 3
        
        # Cetak nilai rata-rata
        print(f"Nilai rata-rata: {rata_rata:.2f}")


uts = float(input("Masukkan nilai UTS: "))
utsp = float(input("Masukkan nilai UTSP: "))
uas = float(input("Masukkan nilai UAS: "))
uasp = float(input("Masukkan nilai UASP: "))
b_uts = 0.30
b_utsp = 0.15
b_uas = 0.40
b_uasp = 0.15

na = (uts * b_uts) + (utsp * b_utsp) + (uas * b_uas) + (uasp * b_uasp)
print("Nilai Akhir: ", na)

if na >= 80 and na <= 100:
    h_m = 'A'
elif na >= 70 and na < 80:
    h_m = 'B'
elif na >= 60 and na < 70:
    h_m = 'C'
elif na >= 40 and na < 60:
    h_m = 'D'
else:
    h_m = 'E'

print("Huruf Mutu: ", h_m)