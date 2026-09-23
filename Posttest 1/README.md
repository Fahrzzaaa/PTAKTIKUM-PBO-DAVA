# Sistem Pengelolaan Penjualan Produk Skincare

## Deskripsi

Program ini dibuat menggunakan Python dengan konsep **Object-Oriented Programming (OOP)** untuk mengelola penjualan produk skincare.

Program memiliki 3 class utama, yaitu:

* **Produk** → mengatur data produk dan stok.
* **Pelanggan** → mengatur data pelanggan dan saldo.
* **Penjualan** → mengatur transaksi dan menghitung total pembelian.

Program juga menggunakan atribut **public dan private**, getter, setter, validasi data, instance method, class method, dan static method.

## Tujuan Program

Program ini dibuat untuk:

* Menampilkan data produk dan stok.
* Mengelola data pelanggan dan saldo.
* Menghitung total penjualan.
* Mengubah data menggunakan setter.
* Melakukan validasi data.
* Menghitung diskon.
* Mengelola data umum toko.

## Class yang Digunakan

### 1. Class Produk

Class `Produk` digunakan untuk menyimpan data produk skincare seperti nama, harga, dan stok.

Atribut kelas:

```python
nama_toko
jenis_toko
jumlah_produk
```

Atribut object:

```python
nama
harga
__stok
```

Atribut `__stok` dibuat private agar data stok tidak diubah secara langsung.

### 2. Class Pelanggan

Class `Pelanggan` digunakan untuk menyimpan data pelanggan berupa nama, alamat, dan saldo.

Saldo dibuat private menggunakan:

```python
__saldo
```

Getter digunakan untuk mengambil saldo, sedangkan setter digunakan untuk mengubah saldo. Nilai saldo negatif akan ditolak oleh program.

### 3. Class Penjualan

Class `Penjualan` digunakan untuk mengatur transaksi.

Data yang digunakan yaitu:

```python
pelanggan
produk
jumlah
total
```

Total pembayaran dihitung dengan rumus:

```text
Harga Produk × Jumlah Pembelian
```

## Method yang Digunakan

### Instance Method

Instance method menggunakan `self`.

Contohnya:

```python
def tampilkan(self):
    print("Nama :", self.nama)
```

Method ini digunakan untuk menampilkan informasi dari object.

### Class Method

Class method menggunakan `@classmethod` dan `cls`.

Digunakan untuk mengubah data yang berhubungan dengan class, salah satunya mengubah nama toko.

### Static Method

Static method menggunakan `@staticmethod` dan tidak menggunakan `self` maupun `cls`.

Pada program ini digunakan untuk mengecek apakah harga lebih dari 0.

## Getter dan Setter

Getter digunakan untuk mengambil nilai dari atribut private.

Setter digunakan untuk mengubah nilai atribut private sekaligus melakukan validasi.

Contohnya pada stok:

```python
@property
def stok(self):
    return self.__stok

@stok.setter
def stok(self, nilai):
    if nilai < 0:
        raise ValueError("Stok tidak boleh negatif!")
    self.__stok = nilai
```

Jika stok diberi nilai negatif, program akan menolak perubahan tersebut.

## Object

Program membuat minimal dua object dari setiap class sesuai dengan ketentuan tugas.

Contohnya:

```python
produk1 = Produk("Facial Wash", 35000, 10)
produk2 = Produk("Moisturizer", 50000, 15)
```

Object tersebut digunakan untuk melakukan pengujian terhadap class dan method yang dibuat.

## Pengujian Program

Program melakukan pengujian menggunakan data yang benar dan salah.

Contohnya ketika stok diubah menjadi nilai negatif:

```python
produk1.stok = -5
```

Program akan menampilkan pesan:

```text
Stok tidak boleh negatif!
```

Hal ini menunjukkan bahwa validasi pada setter berjalan dengan baik.

Program juga melakukan pengujian terhadap instance method, class method, dan static method untuk memastikan semua method dapat berjalan.

## Konsep OOP yang Digunakan

Program menerapkan beberapa konsep OOP, yaitu:

* Class dan Object
* Atribut Class
* Atribut Instance
* Atribut Public
* Atribut Private
* Instance Method
* Class Method
* Static Method
* Getter dan Setter
* Validasi Data

## Identitas

**Nama:** Muhammad Dava Fahriza
**NIM:** 2509106100
**Kelas:** C1'26
**Program Studi:** Informatika
**Universitas:** Universitas Mulawarman
