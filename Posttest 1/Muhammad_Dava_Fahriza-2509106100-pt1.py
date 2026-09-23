class Produk:
    nama_toko = "Glow Skincare"
    jenis_toko = "Skincare"
    jumlah_produk = 0

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga

        self.__stok = stok

        Produk.jumlah_produk += 1

    def tampilkan(self):
        print("Nama  :", self.nama)
        print("Harga : Rp", self.harga)
        print("Stok  :", self.__stok)

    @property
    def stok(self):
        return self.__stok

    @stok.setter
    def stok(self, nilai):
        if nilai < 0:
            raise ValueError("Stok tidak boleh negatif!")
        self.__stok = nilai

    @classmethod
    def ganti_nama_toko(cls, nama):
        if nama.strip() == "":
            raise ValueError("Nama toko tidak boleh kosong!")

        cls.nama_toko = nama

    @staticmethod
    def cek_harga(harga):
        return harga > 0


class Pelanggan:

    nama_toko = "Glow Skincare"
    jumlah_pelanggan = 0
    status_toko = "Aktif"

    def __init__(self, nama, alamat, saldo):
        self.nama = nama
        self.alamat = alamat
        self.__saldo = saldo

        Pelanggan.jumlah_pelanggan += 1

    def tampilkan(self):
        print("Nama   :", self.nama)
        print("Alamat :", self.alamat)
        print("Saldo  : Rp", self.__saldo)

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            raise ValueError("Saldo tidak boleh negatif!")

        self.__saldo = nilai

    @classmethod
    def tampilkan_total(cls):
        print("Jumlah pelanggan:", cls.jumlah_pelanggan)

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""


class Penjualan:
    nama_toko = "Glow Skincare"
    jumlah_transaksi = 0
    pajak = 0.10

    def __init__(self, pelanggan, produk, jumlah):
        self.pelanggan = pelanggan
        self.produk = produk
        self.jumlah = jumlah
        self.__total = 0

        Penjualan.jumlah_transaksi += 1

    def hitung_total(self):
        self.__total = self.produk.harga * self.jumlah
        return self.__total

    @property
    def total(self):
        return self.__total

    @total.setter
    def total(self, nilai):
        if nilai < 0:
            raise ValueError("Total tidak boleh negatif!")

        self.__total = nilai

    @classmethod
    def ubah_pajak(cls, pajak):
        if pajak < 0:
            raise ValueError("Pajak tidak boleh negatif!")

        cls.pajak = pajak

    @staticmethod
    def hitung_diskon(harga, persen):
        if harga < 0 or persen < 0:
            raise ValueError("Harga dan diskon tidak boleh negatif!")

        return harga - (harga * persen / 100)

print("=" * 50)
print(" SISTEM PENGELOLAAN PENJUALAN PRODUK SKINCARE")
print("=" * 50)


print("\n--- DATA PRODUK ---")

produk1 = Produk("Facial Wash", 35000, 10)
produk2 = Produk("Moisturizer", 50000, 15)

produk1.tampilkan()
print()
produk2.tampilkan()

print("\nStok produk 1:", produk1.stok)

produk1.stok = 20
print("Stok setelah diubah:", produk1.stok)

try:
    produk1.stok = -5
except ValueError as e:
    print("Validasi:", e)


Produk.ganti_nama_toko("Glow Beauty")
print("Nama toko:", Produk.nama_toko)


print("Harga Rp35.000 valid:",
      Produk.cek_harga(35000))


print("\n--- DATA PELANGGAN ---")

pelanggan1 = Pelanggan("Dava", "Balikpapan", 100000)
pelanggan2 = Pelanggan("Meyssa", "Samarinda", 150000)

pelanggan1.tampilkan()

print()

pelanggan2.tampilkan()


print("\nSaldo pelanggan 1:", pelanggan1.saldo)

pelanggan1.saldo = 200000
print("Saldo setelah diubah:", pelanggan1.saldo)

try:
    pelanggan1.saldo = -10000
except ValueError as e:
    print("Validasi:", e)


Pelanggan.tampilkan_total()


print("Nama Dava valid:",
      Pelanggan.cek_nama("Dava"))


print("\n--- DATA PENJUALAN ---")

penjualan1 = Penjualan(pelanggan1, produk1, 2)
penjualan2 = Penjualan(pelanggan2, produk2, 3)


print("Total penjualan 1: Rp",
      penjualan1.hitung_total())

print("Total penjualan 2: Rp",
      penjualan2.hitung_total())

print("\nGetter total penjualan 1:",
      penjualan1.total)

penjualan1.total = 70000
print("Total setelah diubah:",
      penjualan1.total)


try:
    penjualan1.total = -5000
except ValueError as e:
    print("Validasi:", e)


Penjualan.ubah_pajak(0.11)

print("Pajak toko:",
      Penjualan.pajak * 100, "%")


harga = Penjualan.hitung_diskon(100000, 10)

print("Harga Rp100.000 setelah diskon 10%: Rp",
      harga)

print("\n--- DATA UMUM ---")

print("Nama toko       :", Produk.nama_toko)
print("Jenis toko      :", Produk.jenis_toko)
print("Jumlah produk   :", Produk.jumlah_produk)
print("Jumlah pelanggan:", Pelanggan.jumlah_pelanggan)
print("Jumlah transaksi:", Penjualan.jumlah_transaksi)

print("\n" + "=" * 50)
print(" PROGRAM SELESAI")
print("=" * 50)
