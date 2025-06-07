# ============================================
# Program Prediksi Jurusan Mahasiswa Baru
# ============================================

# ----------- FUNGSI UTAMA PROGRAM -----------

def tampilkan_menu():
    print("\n======= MENU UTAMA =======")
    print("1. Prediksi Jurusan")
    print("2. Lihat Riwayat Prediksi")
    print("3. Statistik Prediksi")
    print("4. Keluar")

def jalankan_menu():
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-4): ")
        if pilihan == '1':
            prediksi_jurusan()
        elif pilihan == '2':
            tampilkan_log()
        elif pilihan == '3':
            tampilkan_statistik()
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

# ----------- FUNGSI INPUT & VALIDASI -----------

def validasi_input_angka(pesan, min_value, max_value):
    while True:
        nilai = input(pesan)
        if nilai.replace('.', '', 1).isdigit():
            nilai = float(nilai)
            if min_value <= nilai <= max_value:
                return nilai
            else:
                print(f"Nilai harus antara {min_value} dan {max_value}.")
        else:
            print("Input tidak valid. Masukkan angka.")

def input_data():
    print("\n--- Input Data Calon Mahasiswa ---")
    while True:
        jurusan = input("Jurusan SMA (IPA/IPS)             : ").strip().upper()
        if jurusan in ['IPA', 'IPS']:
            break
        else:
            print("Input tidak valid. Masukkan IPA atau IPS.")
    rata_rata = validasi_input_angka("Rata-rata Nilai SMA (0-100)       : ", 0, 100)
    nilai_utbk = validasi_input_angka("Nilai UTBK (0-100)                : ", 0, 100)
    return jurusan, rata_rata, nilai_utbk

# ----------- LOGIKA DECISION TREE -----------

def pohon_keputusan(jurusan_sma, rata_rata_sma, nilai_utbk):
    if rata_rata_sma <= 75:
        return "Tidak Diterima"
    else:
        if jurusan_sma == "IPS":
            return "Sistem Informasi"
        else:
            if nilai_utbk <= 75:
                return "RPL"
            elif nilai_utbk <= 85:
                return "Sains Data"
            else:
                return "Informatika"

def penjelasan_label(label):
    penjelasan = {
        "Tidak Diterima": "Nilai rata-rata Anda tidak memenuhi syarat.",
        "Sistem Informasi": "Cocok untuk siswa IPS yang ingin belajar teknologi dan bisnis.",
        "RPL": "Fokus pada pengembangan perangkat lunak dan pemrograman.",
        "Sains Data": "Mempelajari analisis data dan machine learning.",
        "Informatika": "Jurusan teknik yang mendalami sistem, algoritma, dan coding."
    }
    return penjelasan.get(label, "Tidak ada penjelasan.")

# ----------- FUNGSI PREDIKSI -----------

def prediksi_jurusan():
    jurusan_sma, rata_rata_sma, nilai_utbk = input_data()
    hasil = pohon_keputusan(jurusan_sma, rata_rata_sma, nilai_utbk)

    print("\n=== HASIL PREDIKSI ===")
    print(f"Jurusan SMA        : {jurusan_sma}")
    print(f"Rata-rata SMA      : {rata_rata_sma}")
    print(f"Nilai UTBK         : {nilai_utbk}")
    print(f"Prediksi Jurusan   : {hasil}")
    print("Penjelasan         :", penjelasan_label(hasil))

    simpan_log(jurusan_sma, rata_rata_sma, nilai_utbk, hasil)

# ----------- FUNGSI LOGGING (tanpa os) -----------

def file_ada(nama_file):
    try:
        f = open(nama_file, "r")
        f.close()
        return True
    except:
        return False

def simpan_log(jurusan_sma, rata_rata, utbk, hasil):
    try:
        f = open("log_prediksi.txt", "a")
        f.write(f"{jurusan_sma},{rata_rata},{utbk},{hasil}\n")
        f.close()
    except:
        print("Gagal menyimpan log.")

def tampilkan_log():
    print("\n=== Riwayat Prediksi ===")
    if not file_ada("log_prediksi.txt"):
        print("Belum ada data prediksi.")
        return
    f = open("log_prediksi.txt", "r")
    lines = f.readlines()
    f.close()

    if not lines:
        print("Belum ada data prediksi.")
    else:
        print("No | Jurusan | Rata-rata | UTBK | Hasil")
        print("-------------------------------------------")
        for i, line in enumerate(lines, 1):
            data = line.strip().split(",")
            print(f"{i:2} | {data[0]:7} | {data[1]:10} | {data[2]:5} | {data[3]}")

# ----------- FUNGSI STATISTIK -----------

def tampilkan_statistik():
    print("\n=== Statistik Prediksi ===")
    if not file_ada("log_prediksi.txt"):
        print("Belum ada data untuk statistik.")
        return

    hasil_count = {
        "Tidak Diterima": 0,
        "Sistem Informasi": 0,
        "RPL": 0,
        "Sains Data": 0,
        "Informatika": 0
    }

    f = open("log_prediksi.txt", "r")
    lines = f.readlines()
    f.close()

    for line in lines:
        data = line.strip().split(",")
        label = data[-1]
        if label in hasil_count:
            hasil_count[label] += 1

    total = sum(hasil_count.values())
    if total == 0:
        print("Belum ada data untuk dihitung.")
        return

    for label, count in hasil_count.items():
        persentase = (count / total) * 100
        print(f"{label:17}: {count} data ({persentase:.1f}%)")

# ----------- PROGRAM UTAMA -----------

if __name__ == "__main__":
    print("=" * 40)
    print("SISTEM PREDIKSI JURUSAN MAHASISWA BARU")
    print("Berdasarkan Decision Tree Sederhana")
    print("=" * 40)
    jalankan_menu()
