# Sistem Pengelolaan Penjualan Produk Skincare

## Deskripsi
Program ini merupakan sistem pengelolaan penjualan produk skincare berbasis Python yang menerapkan konsep Object-Oriented Programming (OOP). Program digunakan untuk menampilkan produk, mengelola data pelanggan, melakukan transaksi penjualan, menghitung diskon dan pajak, serta menampilkan laporan penjualan dan notifikasi.

## Fitur Program
- Menampilkan daftar produk skincare wajah dan tubuh.
- Menampilkan data pelanggan member dan non-member.
- Melakukan transaksi pembelian produk.
- Menghitung harga, diskon, pajak, dan total pembayaran.
- Memeriksa saldo pelanggan dan stok produk.
- Menampilkan laporan penjualan dan notifikasi.

## UML Class Diagram

![UML Class Diagram Sistem Pengelolaan Penjualan Produk Skincare](uml.png)

Gambar UML di atas menunjukkan hubungan antarclass dalam program, termasuk inheritance, association, aggregation, dan composition.

### Penjelasan Relasi UML

**1. Association (Asosiasi)**

Class `Penjualan` berhubungan dengan class `Pelanggan` karena transaksi dilakukan oleh pelanggan. Data pelanggan digunakan untuk menghitung diskon, memeriksa saldo, dan memproses pembayaran.

**2. Aggregation (Agregasi)**

Class `Penjualan` menggunakan objek `Produk` yang sudah dibuat sebelumnya dalam daftar produk. Objek produk tersebut dapat tetap digunakan meskipun tidak ada transaksi yang berlangsung.

**3. Composition (Komposisi)**

Class `Penjualan` membuat objek `DetailPenjualan` di dalam konstruktor. Detail penjualan menyimpan informasi produk dan jumlah pembelian yang digunakan untuk menghitung subtotal transaksi.

**4. Inheritance (Pewarisan)**

Program menerapkan pewarisan pada dua kelompok class. `SkincareWajah` dan `SkincareTubuh` mewarisi class `Produk`, sedangkan `PelangganMember` dan `PelangganNonMember` mewarisi class `Pelanggan`. Subclass menggunakan `super().__init__()` untuk memanggil konstruktor class induk.

## Penerapan Abstraction

Abstraction diterapkan melalui class abstrak `Produk` yang menggunakan modul `abc`, yaitu `ABC` dan `abstractmethod`.

Class `Produk` memiliki dua abstract method:
- `hitung_harga()`
- `tampilkan_info()`

Kedua method tersebut wajib diimplementasikan oleh subclass `SkincareWajah` dan `SkincareTubuh`. Class `Produk` juga memiliki method konkret `jalankan()` yang dapat digunakan oleh subclass.

Program membuktikan bahwa class abstrak tidak dapat dibuat menjadi objek secara langsung. Ketika program mencoba membuat objek `Produk`, kesalahan `TypeError` ditangkap menggunakan `try-except`.

## Penerapan Polymorphism

Polymorphism diterapkan melalui method yang sama tetapi memiliki perilaku berbeda.

### 1. Method Overriding

Method `hitung_harga()` pada `SkincareWajah` mengembalikan harga asli, sedangkan pada `SkincareTubuh` mengembalikan harga setelah diskon 5%.

Method `hitung_diskon()` juga memiliki perilaku berbeda pada `PelangganMember` dan `PelangganNonMember`. Member memperoleh diskon sesuai nilai yang diberikan, sedangkan non-member tidak memperoleh diskon.

Perbedaan perilaku tersebut ditampilkan melalui perulangan yang memanggil method pada objek dari subclass yang berbeda.

### 2. Duck Typing

Duck typing diterapkan pada class `LaporanPenjualan` dan `Notifikasi`. Kedua class tersebut tidak memiliki hubungan pewarisan, tetapi sama-sama mempunyai method `tampilkan()`.

Keduanya dipanggil menggunakan fungsi yang sama:

`proses_tampilan(objek)`

Fungsi tersebut dapat menerima objek berbeda selama objek memiliki method `tampilkan()`.

### 3. Operator Overloading

Operator overloading diterapkan melalui method khusus `__str__()` pada class `DetailPenjualan`. Method ini menentukan representasi teks objek ketika ditampilkan menggunakan fungsi `str()` atau `print()`.

Contohnya, detail pembelian dapat ditampilkan dalam bentuk `Facial Wash x 2`.

## Konsep OOP Lainnya

- **Encapsulation:** atribut `__stok`, `__kode`, dan `__saldo` menggunakan atribut private. Atribut `_nama` dan `_alamat` menggunakan konvensi protected.
- **Inheritance:** subclass menggunakan konstruktor class induk melalui `super().__init__()`.
- **Class Method:** digunakan untuk mengubah nama toko, menampilkan jumlah pelanggan, dan mengubah pajak.
- **Static Method:** digunakan untuk memeriksa harga dan nama serta menghitung diskon.
- **Property:** digunakan untuk mengakses dan mengubah stok produk serta saldo pelanggan dengan validasi.
- **Exception Handling:** menggunakan `try-except` untuk menangani kesalahan abstraksi dan input transaksi.

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Simpan kode program dengan nama `main.py`.
3. Buka terminal pada folder tempat file disimpan.
4. Jalankan perintah berikut:

```bash
python main.py
```

Jika menggunakan Windows dan perintah tersebut tidak berhasil, coba:

```bash
py main.py
```

## Screenshot Output

Tambahkan screenshot hasil program pada bagian berikut setelah program dijalankan.

### 1. Bukti Abstraction

Masukkan screenshot terminal yang menunjukkan bahwa objek `Produk` tidak dapat dibuat langsung dan kesalahan `TypeError` berhasil ditangkap.

### 2. Daftar Produk

Masukkan screenshot hasil menu untuk menampilkan produk skincare wajah dan tubuh.

### 3. Daftar Pelanggan

Masukkan screenshot yang menampilkan informasi pelanggan member dan non-member.

### 4. Transaksi Penjualan

Masukkan screenshot transaksi yang berhasil, termasuk subtotal, diskon, pajak, total pembayaran, dan sisa saldo.

### 5. Laporan dan Notifikasi

Masukkan screenshot hasil menu laporan penjualan dan notifikasi.

## Kesimpulan

Program Sistem Pengelolaan Penjualan Produk Skincare menerapkan konsep OOP menggunakan Python, meliputi abstraction, encapsulation, inheritance, polymorphism, duck typing, dan operator overloading. Program ini juga menerapkan relasi UML berupa association, aggregation, dan composition untuk menggambarkan hubungan antarclass dalam sistem penjualan.
