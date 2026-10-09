from linked_list import DoubleLinkedList

dll = DoubleLinkedList()

def menu():
    while True:
        print("\n=== PROGRAM MANAJEMEN DATA MAHASISWA ===")
        print("1. Tambah di Awal")
        print("2. Tambah di Akhir")
        print("3. Tambah Urut NIM (Tengah)")
        print("4. Hapus Data by NIM")
        print("5. Cari Data by NIM")
        print("6. Tampilkan Semua Data")
        print("0. Keluar")

        pilih = input("Pilih menu: ")

        # Menu 1, 2, dan 3
        if pilih == '1' or pilih == '2' or pilih == '3':

            nim = int(input("Masukkan NIM (angka): "))
            nama = input("Masukkan Nama: ")
            jurusan = input("Masukkan Jurusan: ")

            if pilih == '1':
                dll.tambah_awal(nim, nama, jurusan)

            if pilih == '2':
                dll.tambah_akhir(nim, nama, jurusan)

            if pilih == '3':
                dll.tambah_urut_nim(nim, nama, jurusan)


        # Menu 4
        elif pilih == '4':

            nim = int(input("Masukkan NIM yang akan dihapus: "))
            dll.hapus_nim(nim)


        # Menu 5
        elif pilih == '5':

            nim = int(input("Masukkan NIM yang dicari: "))
            hasil = dll.cari_nim(nim)

            if hasil:
                print(
                    f"DITEMUKAN: {hasil.nim} - "
                    f"{hasil.nama} - "
                    f"{hasil.jurusan}"
                )
            else:
                print("Data tidak ditemukan")

        # Menu 6
        elif pilih == '6':

            dll.tampilkan()


        # Menu 0
        elif pilih == '0':

            print("Terima kasih!")
            break

        else:

            print("Pilihan tidak valid")

if __name__ == "__main__":
    menu()