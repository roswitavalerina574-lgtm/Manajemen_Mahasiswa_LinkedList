class Node:
    def _init_(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def _init_(self):
        self.head = None

    def tambah_awal(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        print("Berhasil tambah di awal!")

    def tambah_akhir(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
            new_node.prev = curr
        print("Berhasil tambah di akhir!")

    def tambah_urut_nim(self, nim, nama, jurusan):
        new_node = Node(nim, nama, jurusan)
        if self.head is None or nim < self.head.nim:
            self.tambah_awal(nim, nama, jurusan)
            return
        curr = self.head
        while curr.next and curr.next.nim < nim:
            curr = curr.next
        new_node.next = curr.next
        new_node.prev = curr
        if curr.next:
            curr.next.prev = new_node
        curr.next = new_node
        print(f"Berhasil tambah urut NIM {nim}!")

    def hapus_by_nim(self, nim):
        if not self.head:
            print("Data kosong!")
            return
        curr = self.head
        while curr and curr.nim != nim:
            curr = curr.next
        if not curr:
            print(f"NIM {nim} tidak ada!")
            return
        if curr.prev:
            curr.prev.next = curr.next
        else:
            self.head = curr.next
        if curr.next:
            curr.next.prev = curr.prev
        print(f"NIM {nim} dihapus!")

    def cari_by_nim(self, nim):
        curr = self.head
        while curr:
            if curr.nim == nim:
                return curr
            curr = curr.next
        return None

    def tampilkan(self):
        if not self.head:
            print("Belum ada data!")
            return
        print("-"*60)
        print(f"{'NIM':<10} | {'NAMA':<20} | {'JURUSAN':<20}")
        print("-"*60)
        curr = self.head
        while curr:
            print(f"{curr.nim:<10} | {curr.nama:<20} | {curr.jurusan:<20}")
            curr = curr.next
        print("-"*60)