# 📘 Aplikasi Manajemen Matakuliah (Pyramid)

## Deskripsi Proyek
Aplikasi Manajemen Matakuliah adalah aplikasi **REST API sederhana** yang dibangun menggunakan **Framework Pyramid** dan **SQLAlchemy**.  
Aplikasi ini digunakan untuk melakukan pengelolaan data matakuliah, meliputi **menambah, melihat, mengubah, dan menghapus data matakuliah** melalui API.

Aplikasi ini dibuat sebagai bagian dari **Tugas Praktikum Pemrograman Web**.

---

## ⚙️ Cara Instalasi

### 1️⃣ Membuat Virtual Environment
```bash
python -m venv env
```

Aktifkan environment

**Window**
```bash
env\Scripts\activate
```

**Linux/MacOS**
```bash
source env/bin/activate
```

### 2️⃣ Instalasi Dependensi
```bash
pip install pyramid sqlalchemy alembic waitress
```

### 3️⃣ Konfigurasi Database
Aplikasi menggunakan SQLite sebagai database.

Konfigurasi database berada di file `development.ini`:
```bash
sqlalchemy.url = sqlite:///development.sqlite
```
---

## ▶️ Cara Menjalankan Aplikasi

### 1️⃣ Menjalankan Migrasi Database
```bash
python -m alembic upgrade head
```
Perintah ini akan membuat tabel `matakuliah` di database.

###2️⃣ Menjalankan Server
Dari root project:
```bash
python -m pyramid.scripts.pserve aplikasi_mk/development.ini --reload
```
Server akan berjalan di:
```bash
http://127.0.0.1:6543
```

## 🔗 API Endpoints

**1. Get All Matakuliah**
Mengambil seluruh data matakuliah.
**Request**
```bash
GET /api/matakuliah
```
**Contoh curl**
```bash
curl -X GET http://localhost:6543/api/matakuliah
```
**Response**
[
  {
    "id": 1,
    "kode_mk": "IF101",
    "nama_mk": "Algoritma dan Pemrograman",
    "sks": 3,
    "semester": 1
  }
]

**2. Get Detail Matakuliah**
Mengambil detail matakuliah berdasarkan ID.
**Request**
```bash
GET /api/matakuliah/{id}
```
**Contoh curl**
```bash
curl -X GET http://localhost:6543/api/matakuliah/1
```
**Response**
```bash
{
  "id": 1,
  "kode_mk": "IF101",
  "nama_mk": "Algoritma dan Pemrograman",
  "sks": 3,
  "semester": 1
}
```

**3. Tambah Matakuliah**
Menambahkan data matakuliah baru.
**Request**
```bash
POST /api/matakuliah
```
**Contoh curl**
```bash
curl -X POST http://localhost:6543/api/matakuliah \
-H "Content-Type: application/json" \
-d '{
  "kode_mk": "IF102",
  "nama_mk": "Struktur Data",
  "sks": 3,
  "semester": 2
}'
```
**Respons**
```bash
{
  "message": "Matakuliah berhasil ditambahkan"
}
```

**4. Update Matakuliah**
Mengupdate data matakuliah berdasarkan ID.
**Request**
```bash
PUT /api/matakuliah/{id}
```
**Contoh curl**
```bash
curl -X PUT http://localhost:6543/api/matakuliah/1 \
-H "Content-Type: application/json" \
-d '{
  "kode_mk": "IF101",
  "nama_mk": "Algoritma Lanjut",
  "sks": 3,
  "semester": 1
}'
```
**Response**
```bash
{
  "message": "Matakuliah berhasil diupdate"
}
```

**5. Delete Matakuliah**
Menghapus data matakuliah berdasarkan ID.
**Request**
```bash
DELETE /api/matakuliah/{id}
```
**Contoh curl**
```bash
curl -X DELETE http://localhost:6543/api/matakuliah/1
```
**Response**
```bash
{
  "message": "Matakuliah berhasil dihapus"
}
```

---

## 🧪 Testing
Pengujian API dilakukan menggunakan:
* Postman
* curl
  
Seluruh endpoint telah diuji dan menghasilkan response sesuai dengan yang diharapkan.
