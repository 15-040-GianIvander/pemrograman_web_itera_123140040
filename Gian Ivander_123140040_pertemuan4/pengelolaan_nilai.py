<<<<<<< HEAD
# pengelolaan_nilai.py
from typing import List, Dict, Tuple, Optional

# ===== Data awal (minimal 5 mahasiswa) =====
mahasiswa_list: List[Dict] = [
    {"nama": "Annisa",  "nim": "071", "nilai_uts": 100, "nilai_uas": 100, "nilai_tugas": 100},
    {"nama": "Saud",  "nim": "049", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 60},
    {"nama": "Dzaky", "nim": "039", "nilai_uts": 88, "nilai_uas": 90, "nilai_tugas": 85},
    {"nama": "Regan",  "nim": "047", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
    {"nama": "Anggi",   "nim": "105", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 48},
]

# ===== Fungsi perhitungan & utilitas =====
def hitung_nilai_akhir(mhs: Dict) -> float:
    """
    Hitung nilai akhir dengan bobot:
      - UTS  30%
      - UAS  40%
      - Tugas 30%
    Mengembalikan nilai dengan 2 desimal.
    """
    uts = float(mhs.get("nilai_uts", 0))
    uas = float(mhs.get("nilai_uas", 0))
    tugas = float(mhs.get("nilai_tugas", 0))
    # Hitungan: 0.30*uts + 0.40*uas + 0.30*tugas
    akhir = 0.30 * uts + 0.40 * uas + 0.30 * tugas
    return round(akhir, 2)

def tentukan_grade(nilai_akhir: float) -> str:
    """
    Grade:
      A: >=80
      B: >=70
      C: >=60
      D: >=50
      E: <50
    """
    if nilai_akhir >= 80:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 60:
        return "C"
    if nilai_akhir >= 50:
        return "D"
    return "E"

def data_lengkap(mhs: Dict) -> Dict:
    """Return copy dari mhs dengan tambahan 'nilai_akhir' dan 'grade'."""
    akhir = hitung_nilai_akhir(mhs)
    hasil = mhs.copy()
    hasil["nilai_akhir"] = akhir
    hasil["grade"] = tentukan_grade(akhir)
    return hasil

# ===== Tampilkan tabel rapi =====
def tampilkan_tabel(data: List[Dict]) -> None:
    """Tampilkan list mahasiswa dalam format tabel."""
    if not data:
        print(">> Tidak ada data untuk ditampilkan.")
        return

    # Buat baris lengkap
    rows = []
    for i, m in enumerate(data, start=1):
        d = data_lengkap(m)
        rows.append([
            str(i),
            d["nama"],
            d["nim"],
            f"{d['nilai_uts']:.0f}" if isinstance(d['nilai_uts'], (int, float)) else str(d['nilai_uts']),
            f"{d['nilai_uas']:.0f}" if isinstance(d['nilai_uas'], (int, float)) else str(d['nilai_uas']),
            f"{d['nilai_tugas']:.0f}" if isinstance(d['nilai_tugas'], (int, float)) else str(d['nilai_tugas']),
            f"{d['nilai_akhir']:.2f}",
            d["grade"]
        ])

    headers = ["No", "Nama", "NIM", "UTS", "UAS", "Tugas", "Akhir", "Grade"]
    # Hitung lebar kolom
    col_widths = [max(len(row[col]) for row in ([headers] + rows)) for col in range(len(headers))]
    # Cetak header
    header_line = " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
    sep = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep)
    # Cetak baris
    for row in rows:
        print(" | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))))

# ===== Cari nilai tertinggi / terendah =====
def cari_tertinggi_terendah(data: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Mengembalikan tuple (list_tertinggi, list_terendah).
    Bisa berisi lebih dari satu elemen jika ada nilai sama.
    """
    if not data:
        return [], []
    nilai_pairs = [(hitung_nilai_akhir(m), m) for m in data]
    max_nilai = max(nilai_pairs, key=lambda x: x[0])[0]
    min_nilai = min(nilai_pairs, key=lambda x: x[0])[0]
    tertinggi = [m for nilai, m in nilai_pairs if nilai == max_nilai]
    terendah = [m for nilai, m in nilai_pairs if nilai == min_nilai]
    return tertinggi, terendah

# ===== Tambah mahasiswa baru (input user) =====
def read_float_between(prompt: str, min_v: float = 0.0, max_v: float = 100.0) -> float:
    """Baca input float dengan validasi rentang [min_v, max_v]."""
    while True:
        val = input(prompt).strip()
        try:
            f = float(val)
            if f < min_v or f > max_v:
                print(f"Nilai harus antara {min_v} dan {max_v}. Coba lagi.")
                continue
            # jika input integer-like, simpan sebagai float juga
            return f
        except ValueError:
            print("Masukkan angka yang valid (contoh: 78 atau 78.5).")

def tambah_mahasiswa(data: List[Dict]) -> None:
    """Input mahasiswa baru dan append ke list data."""
    print("\n-- Tambah Mahasiswa Baru --")
    nama = input("Nama       : ").strip() or "Unnamed"
    nim = input("NIM        : ").strip() or "N/A"
    uts = read_float_between("Nilai UTS  : ")
    uas = read_float_between("Nilai UAS  : ")
    tugas = read_float_between("Nilai Tugas: ")
    data.append({
        "nama": nama,
        "nim": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas
    })
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.\n")

# ===== Filter berdasarkan grade =====
def filter_berdasarkan_grade(data: List[Dict], grade: str) -> List[Dict]:
    g = grade.upper()
    if g not in {"A","B","C","D","E"}:
        return []
    return [m for m in data if tentukan_grade(hitung_nilai_akhir(m)) == g]

# ===== Hitung rata-rata nilai kelas =====
def rata_rata_kelas(data: List[Dict]) -> Optional[float]:
    if not data:
        return None
    total = 0.0
    for m in data:
        total += hitung_nilai_akhir(m)
    avg = total / len(data)
    return round(avg, 2)

# ===== Ringkasan singkat =====
def cetak_ringkasan(data: List[Dict]) -> None:
    print("\n-- Ringkasan Kelas --")
    print(f"Jumlah mahasiswa: {len(data)}")
    avg = rata_rata_kelas(data)
    print(f"Rata-rata nilai akhir: {avg if avg is not None else 'N/A'}")
    tertinggi, terendah = cari_tertinggi_terendah(data)
    if tertinggi:
        print("Nilai tertinggi:")
        for m in tertinggi:
            print(f" - {m['nama']} (NIM {m['nim']}): {hitung_nilai_akhir(m):.2f} -> Grade {tentukan_grade(hitung_nilai_akhir(m))}")
    if terendah:
        print("Nilai terendah:")
        for m in terendah:
            print(f" - {m['nama']} (NIM {m['nim']}): {hitung_nilai_akhir(m):.2f} -> Grade {tentukan_grade(hitung_nilai_akhir(m))}")
    print()

# ===== Menu interaktif =====
def menu():
    data = mahasiswa_list
    while True:
        print("\n=== MENU PENGELOLAAN NILAI MAHASISWA ===")
        print("1. Tampilkan semua data (tabel)")
        print("2. Tambah mahasiswa baru")
        print("3. Cari mahasiswa (nilai tertinggi & terendah)")
        print("4. Filter mahasiswa berdasarkan grade")
        print("5. Hitung rata-rata nilai kelas")
        print("6. Cetak ringkasan statistik")
        print("0. Keluar")
        pilihan = input("Pilih (0-6): ").strip()

        if pilihan == "1":
            tampilkan_tabel(data)
        elif pilihan == "2":
            tambah_mahasiswa(data)
        elif pilihan == "3":
            t, r = cari_tertinggi_terendah(data)
            print("\n== Mahasiswa dengan nilai tertinggi ==")
            tampilkan_tabel([m for m in t])
            print("\n== Mahasiswa dengan nilai terendah ==")
            tampilkan_tabel([m for m in r])
        elif pilihan == "4":
            g = input("Masukkan grade (A/B/C/D/E): ").strip().upper()
            if g not in {"A","B","C","D","E"}:
                print("Grade tidak valid.")
            else:
                hasil = filter_berdasarkan_grade(data, g)
                if hasil:
                    tampilkan_tabel(hasil)
                else:
                    print(f"Tidak ada mahasiswa dengan grade {g}.")
        elif pilihan == "5":
            avg = rata_rata_kelas(data)
            if avg is None:
                print("Tidak ada data mahasiswa.")
            else:
                print(f"Rata-rata nilai akhir kelas: {avg:.2f}")
        elif pilihan == "6":
            cetak_ringkasan(data)
        elif pilihan == "0":
            print("Keluar. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak dikenal. Coba lagi.")

# ===== Entry point =====
if __name__ == "__main__":
    menu()
=======
# pengelolaan_nilai.py
from typing import List, Dict, Tuple, Optional

# ===== Data awal (minimal 5 mahasiswa) =====
mahasiswa_list: List[Dict] = [
    {"nama": "Annisa",  "nim": "071", "nilai_uts": 100, "nilai_uas": 100, "nilai_tugas": 100},
    {"nama": "Saud",  "nim": "049", "nilai_uts": 65, "nilai_uas": 70, "nilai_tugas": 60},
    {"nama": "Dzaky", "nim": "039", "nilai_uts": 88, "nilai_uas": 90, "nilai_tugas": 85},
    {"nama": "Regan",  "nim": "047", "nilai_uts": 55, "nilai_uas": 60, "nilai_tugas": 58},
    {"nama": "Anggi",   "nim": "105", "nilai_uts": 45, "nilai_uas": 50, "nilai_tugas": 48},
]

# ===== Fungsi perhitungan & utilitas =====
def hitung_nilai_akhir(mhs: Dict) -> float:
    """
    Hitung nilai akhir dengan bobot:
      - UTS  30%
      - UAS  40%
      - Tugas 30%
    Mengembalikan nilai dengan 2 desimal.
    """
    uts = float(mhs.get("nilai_uts", 0))
    uas = float(mhs.get("nilai_uas", 0))
    tugas = float(mhs.get("nilai_tugas", 0))
    # Hitungan: 0.30*uts + 0.40*uas + 0.30*tugas
    akhir = 0.30 * uts + 0.40 * uas + 0.30 * tugas
    return round(akhir, 2)

def tentukan_grade(nilai_akhir: float) -> str:
    """
    Grade:
      A: >=80
      B: >=70
      C: >=60
      D: >=50
      E: <50
    """
    if nilai_akhir >= 80:
        return "A"
    if nilai_akhir >= 70:
        return "B"
    if nilai_akhir >= 60:
        return "C"
    if nilai_akhir >= 50:
        return "D"
    return "E"

def data_lengkap(mhs: Dict) -> Dict:
    """Return copy dari mhs dengan tambahan 'nilai_akhir' dan 'grade'."""
    akhir = hitung_nilai_akhir(mhs)
    hasil = mhs.copy()
    hasil["nilai_akhir"] = akhir
    hasil["grade"] = tentukan_grade(akhir)
    return hasil

# ===== Tampilkan tabel rapi =====
def tampilkan_tabel(data: List[Dict]) -> None:
    """Tampilkan list mahasiswa dalam format tabel."""
    if not data:
        print(">> Tidak ada data untuk ditampilkan.")
        return

    # Buat baris lengkap
    rows = []
    for i, m in enumerate(data, start=1):
        d = data_lengkap(m)
        rows.append([
            str(i),
            d["nama"],
            d["nim"],
            f"{d['nilai_uts']:.0f}" if isinstance(d['nilai_uts'], (int, float)) else str(d['nilai_uts']),
            f"{d['nilai_uas']:.0f}" if isinstance(d['nilai_uas'], (int, float)) else str(d['nilai_uas']),
            f"{d['nilai_tugas']:.0f}" if isinstance(d['nilai_tugas'], (int, float)) else str(d['nilai_tugas']),
            f"{d['nilai_akhir']:.2f}",
            d["grade"]
        ])

    headers = ["No", "Nama", "NIM", "UTS", "UAS", "Tugas", "Akhir", "Grade"]
    # Hitung lebar kolom
    col_widths = [max(len(row[col]) for row in ([headers] + rows)) for col in range(len(headers))]
    # Cetak header
    header_line = " | ".join(headers[i].ljust(col_widths[i]) for i in range(len(headers)))
    sep = "-+-".join("-" * col_widths[i] for i in range(len(headers)))
    print(header_line)
    print(sep)
    # Cetak baris
    for row in rows:
        print(" | ".join(row[i].ljust(col_widths[i]) for i in range(len(row))))

# ===== Cari nilai tertinggi / terendah =====
def cari_tertinggi_terendah(data: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Mengembalikan tuple (list_tertinggi, list_terendah).
    Bisa berisi lebih dari satu elemen jika ada nilai sama.
    """
    if not data:
        return [], []
    nilai_pairs = [(hitung_nilai_akhir(m), m) for m in data]
    max_nilai = max(nilai_pairs, key=lambda x: x[0])[0]
    min_nilai = min(nilai_pairs, key=lambda x: x[0])[0]
    tertinggi = [m for nilai, m in nilai_pairs if nilai == max_nilai]
    terendah = [m for nilai, m in nilai_pairs if nilai == min_nilai]
    return tertinggi, terendah

# ===== Tambah mahasiswa baru (input user) =====
def read_float_between(prompt: str, min_v: float = 0.0, max_v: float = 100.0) -> float:
    """Baca input float dengan validasi rentang [min_v, max_v]."""
    while True:
        val = input(prompt).strip()
        try:
            f = float(val)
            if f < min_v or f > max_v:
                print(f"Nilai harus antara {min_v} dan {max_v}. Coba lagi.")
                continue
            # jika input integer-like, simpan sebagai float juga
            return f
        except ValueError:
            print("Masukkan angka yang valid (contoh: 78 atau 78.5).")

def tambah_mahasiswa(data: List[Dict]) -> None:
    """Input mahasiswa baru dan append ke list data."""
    print("\n-- Tambah Mahasiswa Baru --")
    nama = input("Nama       : ").strip() or "Unnamed"
    nim = input("NIM        : ").strip() or "N/A"
    uts = read_float_between("Nilai UTS  : ")
    uas = read_float_between("Nilai UAS  : ")
    tugas = read_float_between("Nilai Tugas: ")
    data.append({
        "nama": nama,
        "nim": nim,
        "nilai_uts": uts,
        "nilai_uas": uas,
        "nilai_tugas": tugas
    })
    print(f"Mahasiswa '{nama}' berhasil ditambahkan.\n")

# ===== Filter berdasarkan grade =====
def filter_berdasarkan_grade(data: List[Dict], grade: str) -> List[Dict]:
    g = grade.upper()
    if g not in {"A","B","C","D","E"}:
        return []
    return [m for m in data if tentukan_grade(hitung_nilai_akhir(m)) == g]

# ===== Hitung rata-rata nilai kelas =====
def rata_rata_kelas(data: List[Dict]) -> Optional[float]:
    if not data:
        return None
    total = 0.0
    for m in data:
        total += hitung_nilai_akhir(m)
    avg = total / len(data)
    return round(avg, 2)

# ===== Ringkasan singkat =====
def cetak_ringkasan(data: List[Dict]) -> None:
    print("\n-- Ringkasan Kelas --")
    print(f"Jumlah mahasiswa: {len(data)}")
    avg = rata_rata_kelas(data)
    print(f"Rata-rata nilai akhir: {avg if avg is not None else 'N/A'}")
    tertinggi, terendah = cari_tertinggi_terendah(data)
    if tertinggi:
        print("Nilai tertinggi:")
        for m in tertinggi:
            print(f" - {m['nama']} (NIM {m['nim']}): {hitung_nilai_akhir(m):.2f} -> Grade {tentukan_grade(hitung_nilai_akhir(m))}")
    if terendah:
        print("Nilai terendah:")
        for m in terendah:
            print(f" - {m['nama']} (NIM {m['nim']}): {hitung_nilai_akhir(m):.2f} -> Grade {tentukan_grade(hitung_nilai_akhir(m))}")
    print()

# ===== Menu interaktif =====
def menu():
    data = mahasiswa_list
    while True:
        print("\n=== MENU PENGELOLAAN NILAI MAHASISWA ===")
        print("1. Tampilkan semua data (tabel)")
        print("2. Tambah mahasiswa baru")
        print("3. Cari mahasiswa (nilai tertinggi & terendah)")
        print("4. Filter mahasiswa berdasarkan grade")
        print("5. Hitung rata-rata nilai kelas")
        print("6. Cetak ringkasan statistik")
        print("0. Keluar")
        pilihan = input("Pilih (0-6): ").strip()

        if pilihan == "1":
            tampilkan_tabel(data)
        elif pilihan == "2":
            tambah_mahasiswa(data)
        elif pilihan == "3":
            t, r = cari_tertinggi_terendah(data)
            print("\n== Mahasiswa dengan nilai tertinggi ==")
            tampilkan_tabel([m for m in t])
            print("\n== Mahasiswa dengan nilai terendah ==")
            tampilkan_tabel([m for m in r])
        elif pilihan == "4":
            g = input("Masukkan grade (A/B/C/D/E): ").strip().upper()
            if g not in {"A","B","C","D","E"}:
                print("Grade tidak valid.")
            else:
                hasil = filter_berdasarkan_grade(data, g)
                if hasil:
                    tampilkan_tabel(hasil)
                else:
                    print(f"Tidak ada mahasiswa dengan grade {g}.")
        elif pilihan == "5":
            avg = rata_rata_kelas(data)
            if avg is None:
                print("Tidak ada data mahasiswa.")
            else:
                print(f"Rata-rata nilai akhir kelas: {avg:.2f}")
        elif pilihan == "6":
            cetak_ringkasan(data)
        elif pilihan == "0":
            print("Keluar. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak dikenal. Coba lagi.")

# ===== Entry point =====
if __name__ == "__main__":
    menu()
>>>>>>> f72dbe99ced344981b147ddf0515794376319e9f
