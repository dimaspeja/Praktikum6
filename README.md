# Program Manajemen Data Mahasiswa

Program ini merupakan aplikasi sederhana berbasis terminal untuk mengelola data mahasiswa menggunakan struktur data **dictionary** di Python.  
Fitur yang tersedia meliputi:

- Tambah Data  
- Tampilkan Data  
- Hapus Data  
- Ubah Data  
- Keluar Program  

---

## 1. Dictionary Utama
```python
mahasiswa = {}
```
Variable mahasiswa adalah dictionary kosong yang akan menyimpan data mahasiswa dalam format:
```python
{
   "Nama" : {"nim": "xxxx", "nilai": xx.xx}
}
```
Contoh setelah diisi:
```python
{
   "Dimas": {"nim": "12345", "nilai": 90}
}
```
## 2. Fungsi tambah()
```python
def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = float(input("Nilai: "))
    mahasiswa[nama] = {"nim": nim, "nilai": nilai}
    print("Data berhasil ditambahkan!\n")
```
Fungsinya:

- Meminta input nama, NIM, dan nilai.
- Menyimpan data tersebut ke dictionary mahasiswa.
- Menampilkan pesan bahwa data berhasil ditambahkan.

Contoh data tersimpan:
```python
mahasiswa["Dimas"] = {"nim": "12345", "nilai": 90}
```
## 3. Fungsi tampilkan()
```python
def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not mahasiswa:
        print("Belum ada data.\n")
        return

    for nama, data in mahasiswa.items():
        print(f"Nama : {nama}")
        print(f"NIM  : {data['nim']}")
        print(f"Nilai: {data['nilai']}\n")
```
Fungsinya:

- Menampilkan seluruh data mahasiswa.
- Jika dictionary kosong → tampilkan pesan "Belum ada data".
- Jika ada data → tampilkan nama, nim, dan nilai satu per satu.

## 4. Fungsi hapus(nama)
```python
def hapus(nama):
    print("\n=== Hapus Data Mahasiswa ===")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan.\n")
```
Fungsinya:

- Menghapus data mahasiswa berdasarkan nama.
- Jika nama ada → data dihapus.
- Jika tidak ada → tampilkan pesan tidak ditemukan.

## 5. Fungsi ubah(nama)
```python
def ubah(nama):
    print("\n=== Ubah Data Mahasiswa ===")
    if nama in mahasiswa:
        print(f"Data lama: {mahasiswa[nama]}")
        nim = input("NIM baru: ")
        nilai = float(input("Nilai baru: "))
        mahasiswa[nama] = {"nim": nim, "nilai": nilai}
        print("Data berhasil diubah!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan.\n")
```
Fungsinya:

- Mengubah NIM dan nilai dari mahasiswa yang datanya sudah ada.
- Jika nama ditemukan → data diupdate.
- Jika tidak ditemukan → beri pesan kesalahan.

## 6. Menu Utama (Perulangan Program)
```python
while True:
    print("=== Menu Program ===")
    print("[1] Tambah Data")
    print("[2] Tampilkan Data")
    print("[3] Hapus Data")
    print("[4] Ubah Data")
    print("[5] Keluar")

    pilih = input("Pilih menu: ")
```
Program berjalan terus menggunakan while True sampai user memilih menu Keluar.

Kemudian pilihan diproses:
```python
if pilih == "1":
    tambah()
elif pilih == "2":
    tampilkan()
elif pilih == "3":
    nama = input("Masukkan nama yang akan dihapus: ")
    hapus(nama)
elif pilih == "4":
    nama = input("Masukkan nama yang akan diubah: ")
    ubah(nama)
elif pilih == "5":
    print("Program selesai.")
    break
else:
    print("Pilihan tidak valid.\n")
```
Penjelasan:

- "1" → tambah data
- "2" → tampilkan data
- "3" → hapus data berdasarkan nama
- "4" → ubah data mahasiswa
- "5" → menghentikan program dengan break
- Input lain → dianggap tidak valid
