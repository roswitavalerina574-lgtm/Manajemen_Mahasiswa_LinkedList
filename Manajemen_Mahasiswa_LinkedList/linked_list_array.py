class Node:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        # TAMBAHAN ARRAY untuk backup data
        self.array_data = [] 

    def tambah_awal(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node
        
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        print(f"[LinkedList & Array] Berhasil tambah {nama} di awal.")

    def tambah_akhir(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        print(f"[LinkedList & Array] Berhasil tambah {nama} di akhir.")

    def tambah_urut(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if not self.head or nim < self.head.nim:
            if self.head:
                new_node.next = self.head
                self.head.prev = new_node
            self.head = new_node
        else:
            curr = self.head
            while curr.next and curr.next.nim < nim:
                curr = curr.next
            new_node.next = curr.next
            new_node.prev = curr
            if curr.next:
                curr.next.prev = new_node
            curr.next = new_node

        # Simpan di array dan urutkan by NIM
        self.array_data.append({"nim": nim, "nama": nama, "jurusan": jurusan})
        self.array_data = sorted(self.array_data, key=lambda x: x["nim"])
        print(f"[LinkedList & Array] Berhasil tambah {nama} secara urut NIM.")

    def hapus_nim(self, nim):
        if not self.head:
            print("Data masih kosong.")
            return
        curr = self.head
        while curr and curr.nim != nim:
            curr = curr.next
        if not curr:
            print(f"NIM {nim} tidak ditemukan.")
            return
        
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev

        # Hapus dari array juga biar sinkron
        self.array_data = [m for m in self.array_data if m["nim"] != nim]
        print(f"[LinkedList & Array] NIM {nim} berhasil dihapus.")

    def tampil_linkedlist(self):
        print("\n--- Tampil dari DOUBLE LINKED LIST ---")
        if not self.head:
            print("Kosong")
            return
        curr = self.head
        while curr:
            print(f"{curr.nim} | {curr.nama} | {curr.jurusan}")
            curr = curr.next

    def tampil_array(self):
        print("\n--- Tampil dari ARRAY ---")
        if not self.array_data:
            print("Array kosong")
            return
        for m in self.array_data:
            print(f"{m['nim']} | {m['nama']} | {m['jurusan']}")
        print(f"Total di array: {len(self.array_data)} data")

    def cari_di_array(self, nim):
        for m in self.array_data:
            if m["nim"] == nim:
                print(f"Ditemukan di ARRAY: {m}")
                return m
        print(f"NIM {nim} tidak ada di ARRAY")
        return None

# === PROGRAM UTAMA DENGAN MENU ===
if __name__ == "__main__":
    dll = DoubleLinkedList()
    
    # Data awal contoh
    dll.tambah_urut(257111048, "Roswita", "Teknik Informatika")
    dll.tambah_urut(257111037, "Valeri", "Sistem Informasi")
    dll.tambah_urut(257111034, " Rina", "TI")

    while True:
        print("\n===== MENU MAHASISWA =====")
        print("1. Tambah Awal")
        print("2. Tambah Akhir")
        print("3. Tambah Urut NIM")
        print("4. Hapus NIM")
        print("5. Tampil Linked List")
        print("6. Tampil Array")
        print("7. Cari di Array")
        print("0. Keluar")
        pilih = input("Pilih: ")

        if pilih == "1":
            nim = int(input("NIM: ")); nama = input("Nama: "); jur = input("Jurusan: ")
            dll.tambah_awal(nim, nama, jur)
        elif pilih == "2":
            nim = int(input("NIM: ")); nama = input("Nama: "); jur = input("Jurusan: ")
            dll.tambah_akhir(nim, nama, jur)
        elif pilih == "3":
            nim = int(input("NIM: ")); nama = input("Nama: "); jur = input("Jurusan: ")
            dll.tambah_urut(nim, nama, jur)
        elif pilih == "4":
            nim = int(input("NIM yang dihapus: "))
            dll.hapus_nim(nim)
        elif pilih == "5":
            dll.tampil_linkedlist()
        elif pilih == "6":
            dll.tampil_array()
        elif pilih == "7":
            nim = int(input("Cari NIM: "))
            dll.cari_di_array(nim)
        elif pilih == "0":
            break