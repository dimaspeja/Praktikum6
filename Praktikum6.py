mahasiswa = {}

def tambah():
    print("\n=== Tambah Data Mahasiswa ===")
    nama = input("Nama: ")
    nim = input("NIM: ")
    nilai = float(input("Nilai: "))
    mahasiswa[nama] = {"nim": nim, "nilai": nilai}
    print("Data berhasil ditambahkan!\n")


def tampilkan():
    print("\n=== Daftar Nilai Mahasiswa ===")
    if not mahasiswa:
        print("Belum ada data.\n")
        return

    for nama, data in mahasiswa.items():
        print(f"Nama : {nama}")
        print(f"NIM  : {data['nim']}")
        print(f"Nilai: {data['nilai']}\n")


def hapus(nama):
    print("\n=== Hapus Data Mahasiswa ===")
    if nama in mahasiswa:
        del mahasiswa[nama]
        print(f"Data '{nama}' berhasil dihapus!\n")
    else:
        print(f"Data '{nama}' tidak ditemukan.\n")


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


while True:
    print("=== Menu Program ===")
    print("[1] Tambah Data")
    print("[2] Tampilkan Data")
    print("[3] Hapus Data")
    print("[4] Ubah Data")
    print("[5] Keluar")

    pilih = input("Pilih menu: ")

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