# Timeline Tugas - Manajemen Tugas Mahasiswa

Aplikasi "Timeline Tugas"membantu mahasiswa mengelola tugas kuliah: menambahkan tugas (nama tugas, mata kuliah, deadline, catatan), menandai selesai/belum selesai, mengedit dan menghapus tugas, serta mencari dan memfilter daftar tugas. Semua data disimpan secara lokal di peramban menggunakan localStorage.

# Fungsi Utama

Aplikasi ini memungkinkan mahasiswa untuk:
- Menambahkan tugas baru (dengan nama tugas, mata kuliah, dan deadline)
- Mengedit dan menghapus tugas
- Menandai tugas sebagai selesai / belum selesai
- Melakukan pencarian dan filter berdasarkan status atau mata kuliah
- Melihat jumlah tugas yang belum diselesaikan
- Menyimpan seluruh data secara otomatis di `localStorage`

# Tampilan Aplikasi

<img width="1913" height="997" alt="Screenshot 2025-10-27 214123" src="https://github.com/user-attachments/assets/00dbda42-c997-4cbd-ba59-0776d8518dbe" />
<center>Tampilan homepage</center>
<img width="1919" height="999" alt="Screenshot 2025-10-27 215154" src="https://github.com/user-attachments/assets/22d5e52c-8c71-45a3-aabf-10a63b00ebcb" />
<center>Aplikasi dapat menambahkan tugas dan memberi tanda sudah dikerjakan</center>
<img width="1919" height="981" alt="Screenshot 2025-10-27 215205" src="https://github.com/user-attachments/assets/84ec4cbf-ab12-4011-8861-300e62bc7e3a" />
<center>Tugas dapat disortir sesuai dengan yang diinginkan</center>

# Cara Menjalankan Aplikasi
1. Unduh atau kloning repository ini https://github.com/15-040-GianIvander/pemrograman_web_itera_123140040/edit/main/Gian%20Ivander_123140040_pertemuan1 
2. Buka file index.html
3. Gunakan aplikasi:
   - Klik "+ Tambah Tugas" untuk menambahkan tugas baru.
   - Centang kotak di kolom status untuk menandai selesai.
   - Klik ikon ✏️ untuk mengedit dan 🗑️ untuk menghapus.
   - Gunakan filter dan pencarian untuk menemukan tugas tertentu.

# Daftar Fitur
- Tambah tugas, menambahkan tugas baru dengan nama, mata kuliah, deadline, ddan catatan
- Edit tugas, mengubah informasi tugas yang sudah ada
- Tanda selesai, menandai tugas selesai atau belum
- Hapus tugas, menghapus tugas dari daftar
- Filter dan pencarian, menyaring berdasarkan status atau mata kuliah
- Hitung tugas, menampilkan jumlah tugas yang belum selesai
- Simpan otomatis, Data tersimpan di "localStorage" browser
- Validasi form, mencegah input kosong atau tanggal tidak valid
- Urutan otomatis, mengurutkan tugas berdasarkan deadline terdekat

# Penjelasan Teknis
## Penyimpanan dengan "localStorage"
Aplikasi ini menggunakan "localStorage" untuk menyimpan data tugas secara lokal di browser pengguna.
Kelebihan:
- Tidak memerlukan database atau server.
- Data tetap tersimpan meskipun halaman direfresh.

Kekurangan:
- Data tidak tersinkron antar perangkat.
- Akan hilang jika pengguna menghapus data browser.

## Validasi Form
Memastikan "Nama tugas" dan"Mata kuliah" tidak boleh kosong, serta "Deadline" harus tanggal yang valid. Apabila terjadi kesalahan, maka akan ditampilkannya pesan kesalahan.
