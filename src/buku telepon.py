class UtilityApp:
    def __init__(self):
        self.kontak = {}

    # 1. Dedduplikasi
    def deduplikasi(self):
        try:
            data = input("Masukkan angka dipisah spasi: ")
            lst = list(map(int, data.split()))
            seen = set()
            hasil = []

            for item in lst:
                if item not in seen:
                    seen.add(item)
                    hasil.append(item)

            print("Hasil:", hasil)
        except ValueError:
            print("Input harus berupa angka!")

    # 2. Intersection
    def intersection(self):
        try:
            data1 = input("List pertama (spasi): ")
            data2 = input("List kedua (spasi): ")
            arr1 = list(map(int, data1.split()))
            arr2 = list(map(int, data2.split()))

            hasil = [x for x in arr1 if x in set(arr2)]
            print("Hasil:", hasil)
        except ValueError:
            print("Input harus berupa angka!")

    # 3. Anagram
    def is_anagram(self):
        s1 = input("String pertama: ")
        s2 = input("String kedua: ")

        if len(s1) != len(s2):
            print("Bukan anagram")
            return

        count = {}
        for char in s1:
            count[char] = count.get(char, 0) + 1

        for char in s2:
            if char not in count or count[char] == 0:
                print("Bukan anagram")
                return
            count[char] -= 1

        print("Anagram!")

    # 4. First Recurring Character
    def first_recurring_char(self):
        s = input("Masukkan string: ")
        seen = set()

        for char in s:
            if char in seen:
                print("Karakter pertama yang berulang:", char)
                return
            seen.add(char)

        print("Tidak ada karakter berulang.")

    # 5. Buku Telepon
    def buku_telepon(self):
        while True:
            print("\n=== MENU BUKU TELEPON ===")
            print("1. Tambah Kontak")
            print("2. Cari Kontak")
            print("3. Tampilkan Semua")
            print("4. Kembali")

            pilih = input("Pilih: ")

            if pilih == "1":
                nama = input("Nama: ")
                nomor = input("Nomor: ")
                if nama.strip() == "" or nomor.strip() == "":
                    print("Nama dan nomor tidak boleh kosong!")
                else:
                    self.kontak[nama] = nomor
                    print("Kontak berhasil ditambahkan!")

            elif pilih == "2":
                nama = input("Nama yang dicari: ")
                if nama in self.kontak:
                    print("Nomor:", self.kontak[nama])
                else:
                    print("Kontak tidak ditemukan.")

            elif pilih == "3":
                if not self.kontak:
                    print("Belum ada kontak.")
                else:
                    for nama, nomor in self.kontak.items():
                        print(nama, "->", nomor)

            elif pilih == "4":
                break

            else:
                print("Pilihan tidak valid!")

    # Menu utama
    def run(self):
        while True:
            print("\n=== MENU UTAMA ===")
            print("1. Dedduplikasi")
            print("2. Intersection")
            print("3. Cek Anagram")
            print("4. First Recurring Character")
            print("5. Buku Telepon")
            print("6. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                self.deduplikasi()
            elif pilihan == "2":
                self.intersection()
            elif pilihan == "3":
                self.is_anagram()
            elif pilihan == "4":
                self.first_recurring_char()
            elif pilihan == "5":
                self.buku_telepon()
            elif pilihan == "6":
                print("Program selesai.")
                break
            else:
                print("Pilihan tidak valid!")


# Jalankan Program
app = UtilityApp()
app.run()
