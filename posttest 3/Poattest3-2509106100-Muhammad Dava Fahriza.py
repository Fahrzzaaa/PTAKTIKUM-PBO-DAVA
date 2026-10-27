from abc import ABC, abstractmethod

class Produk(ABC):
    nama_toko = "Glow Skincare"
    jenis_toko = "Skincare"
    jumlah_produk = 0

    def __init__(self, nama, harga, stok):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0!")
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif!")

        self.nama = nama
        self.harga = harga
        self.__stok = stok
        self.__kode = f"SK{Produk.jumlah_produk + 1:03d}"

        Produk.jumlah_produk += 1

    @abstractmethod
    def hitung_harga(self):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass

    def jalankan(self):
        print("Toko:", Produk.nama_toko)
        print("Kode:", self.__kode)
        self.tampilkan_info()

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
        if not nama.strip():
            raise ValueError("Nama toko tidak boleh kosong!")
        cls.nama_toko = nama

    @staticmethod
    def cek_harga(harga):
        return harga > 0

class SkincareWajah(Produk):
    def __init__(self, nama, harga, stok, jenis_wajah):
        super().__init__(nama, harga, stok)
        self.jenis_wajah = jenis_wajah

    def hitung_harga(self):
        return self.harga

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("Jenis: Skincare Wajah")
        print("Jenis kulit:", self.jenis_wajah)
        print(f"Harga: Rp{self.hitung_harga():,.0f}")
        print("Stok:", self.stok)


class SkincareTubuh(Produk):
    def __init__(self, nama, harga, stok, ukuran):
        super().__init__(nama, harga, stok)
        self.ukuran = ukuran

    def hitung_harga(self):
        return self.harga * 0.95

    def tampilkan_info(self):
        print("Nama:", self.nama)
        print("Jenis: Skincare Tubuh")
        print("Ukuran:", self.ukuran)
        print(f"Harga setelah diskon: Rp{self.hitung_harga():,.0f}")
        print("Stok:", self.stok)


class Pelanggan:
    nama_toko = "Glow Skincare"
    jumlah_pelanggan = 0
    status_toko = "Aktif"

    def __init__(self, nama, alamat, saldo):
        if saldo < 0:
            raise ValueError("Saldo tidak boleh negatif!")

        self._nama = nama
        self._alamat = alamat
        self.__saldo = saldo

        Pelanggan.jumlah_pelanggan += 1

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, nilai):
        if nilai < 0:
            raise ValueError("Saldo tidak boleh negatif!")
        self.__saldo = nilai

    def hitung_diskon(self):
        return 0

    def tampilkan(self):
        print("Nama:", self._nama)
        print("Alamat:", self._alamat)
        print(f"Saldo: Rp{self.saldo:,.0f}")
        print("Diskon:", self.hitung_diskon(), "%")

    @classmethod
    def tampilkan_total(cls):
        print("Jumlah pelanggan:", Pelanggan.jumlah_pelanggan)

    @staticmethod
    def cek_nama(nama):
        return nama.strip() != ""

class PelangganMember(Pelanggan):
    def __init__(self, nama, alamat, saldo, diskon_member):
        super().__init__(nama, alamat, saldo)
        self.diskon_member = diskon_member

    def hitung_diskon(self):
        return self.diskon_member

    def tampilkan(self):
        super().tampilkan()
        print("Status: Member")


class PelangganNonMember(Pelanggan):
    def __init__(self, nama, alamat, saldo, biaya_admin):
        super().__init__(nama, alamat, saldo)
        self.biaya_admin = biaya_admin

    def hitung_diskon(self):
        return 0

    def tampilkan(self):
        super().tampilkan()
        print("Status: Non Member")
        print(f"Biaya admin: Rp{self.biaya_admin:,.0f}")


class DetailPenjualan:
    def __init__(self, produk, jumlah):
        self.produk = produk
        self.jumlah = jumlah

    def subtotal(self):
        return self.produk.hitung_harga() * self.jumlah

    def tampilkan(self):
        print("Produk:", self.produk.nama)
        print("Jumlah:", self.jumlah)
        print(f"Subtotal: Rp{self.subtotal():,.0f}")

    def __str__(self):
        return f"{self.produk.nama} x {self.jumlah}"

class Penjualan:
    nama_toko = "Glow Skincare"
    jumlah_transaksi = 0
    pajak = 0.10

    def __init__(self, pelanggan, produk, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pembelian harus lebih dari 0!")

        if jumlah > produk.stok:
            raise ValueError("Stok produk tidak mencukupi!")

        self.pelanggan = pelanggan
        self.produk = produk
        self.jumlah = jumlah

        self.detail = DetailPenjualan(produk, jumlah)

        self.__total = 0

        Penjualan.jumlah_transaksi += 1

    def hitung_total(self):
        subtotal = self.detail.subtotal()
        diskon = subtotal * self.pelanggan.hitung_diskon() / 100
        setelah_diskon = subtotal - diskon
        pajak = setelah_diskon * Penjualan.pajak

        self.__total = setelah_diskon + pajak
        return self.__total

    def proses_transaksi(self):
        total = self.hitung_total()

        if self.pelanggan.saldo < total:
            print("Transaksi gagal: saldo tidak mencukupi.")
            return False

        if self.jumlah > self.produk.stok:
            print("Transaksi gagal: stok tidak mencukupi.")
            return False

        self.pelanggan.saldo -= total
        self.produk.stok -= self.jumlah

        print("\nTransaksi berhasil!")
        self.tampilkan()
        return True

    def tampilkan(self):
        print("\n========== DETAIL PENJUALAN ==========")
        print("Pelanggan:", self.pelanggan._nama)
        self.detail.tampilkan()
        print(f"Diskon member: {self.pelanggan.hitung_diskon()}%")
        print(f"Pajak: {Penjualan.pajak * 100:.0f}%")
        print(f"Total bayar: Rp{self.__total:,.0f}")
        print(f"Sisa saldo: Rp{self.pelanggan.saldo:,.0f}")

    @property
    def total(self):
        return self.__total

    @classmethod
    def ubah_pajak(cls, pajak):
        if pajak < 0:
            raise ValueError("Pajak tidak boleh negatif!")
        cls.pajak = pajak

    @staticmethod
    def hitung_diskon(harga, persen):
        if harga < 0 or not 0 <= persen <= 100:
            raise ValueError("Harga atau diskon tidak valid!")
        return harga - (harga * persen / 100)

class LaporanPenjualan:
    def tampilkan(self):
        print("\n========== LAPORAN PENJUALAN ==========")
        print("Jumlah transaksi:", Penjualan.jumlah_transaksi)
        print("Jumlah produk:", Produk.jumlah_produk)


class Notifikasi:
    def tampilkan(self):
        print("\nNotifikasi: Terima kasih telah berbelanja!")


def proses_tampilan(objek):
    objek.tampilkan()


def main():
    print("=" * 50)
    print(" SISTEM PENGELOLAAN PENJUALAN PRODUK SKINCARE")
    print("=" * 50)

    try:
        Produk("Contoh", 10000, 5)
    except TypeError as error:
        print("\n=== BUKTI ABSTRAKSI ===")
        print("Produk tidak dapat dibuat langsung.")
        print("Penyebab:", error)

    daftar_produk = [
        SkincareWajah("Facial Wash", 35000, 10, "Berminyak"),
        SkincareWajah("Moisturizer", 50000, 15, "Kering"),
        SkincareTubuh("Body Lotion", 40000, 12, "250 ml"),
        SkincareTubuh("Body Scrub", 60000, 8, "200 gram")
    ]

    pelanggan1 = PelangganMember(
        "Dava", "Balikpapan", 200000, 10
    )

    pelanggan2 = PelangganNonMember(
        "Meyssa", "Samarinda", 250000, 5000
    )

    while True:
        print("\n=============== MENU ===============")
        print("1. Lihat produk")
        print("2. Lihat pelanggan")
        print("3. Transaksi pelanggan")
        print("4. Laporan dan notifikasi")
        print("0. Keluar")

        pilihan = input("Pilih menu: ").strip()

        if pilihan == "1":
            print("\n========== DAFTAR PRODUK ==========")

            for produk in daftar_produk:
                produk.jalankan()
                print("-" * 35)

        elif pilihan == "2":
            print("\n========== DAFTAR PELANGGAN ==========")

            for pelanggan in [pelanggan1, pelanggan2]:
                pelanggan.tampilkan()
                print("-" * 35)

            Pelanggan.tampilkan_total()

        elif pilihan == "3":
            print("\nPilih pelanggan:")
            print("1. Dava (Member)")
            print("2. Meyssa (Non Member)")

            pilih_pelanggan = input("Pilihan: ").strip()

            if pilih_pelanggan == "1":
                pelanggan = pelanggan1
            elif pilih_pelanggan == "2":
                pelanggan = pelanggan2
            else:
                print("Pilihan pelanggan tidak valid.")
                continue

            for i, produk in enumerate(daftar_produk, start=1):
                print(
                    f"{i}. {produk.nama} | "
                    f"Rp{produk.hitung_harga():,.0f} | "
                    f"Stok: {produk.stok}"
                )

            try:
                nomor = int(input("Nomor produk: ")) - 1
                jumlah = int(input("Jumlah beli: "))

                if nomor < 0 or nomor >= len(daftar_produk):
                    print("Nomor produk tidak valid.")
                    continue

                transaksi = Penjualan(
                    pelanggan, daftar_produk[nomor], jumlah
                )

                transaksi.proses_transaksi()

            except ValueError as error:
                print("Transaksi gagal:", error)

        elif pilihan == "4":
            proses_tampilan(LaporanPenjualan())
            proses_tampilan(Notifikasi())

        elif pilihan == "0":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()