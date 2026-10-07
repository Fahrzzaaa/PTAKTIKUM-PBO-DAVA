# POSTTEST 2 PBO

## Sistem Pengelolaan Penjualan Produk Skincare

### Identitas

**Nama:** Muhammad Dava Fahriza
**Tema:** Sistem Pengelolaan Penjualan Produk Skincare
**Posttest:** 2

---

## 1. Deskripsi Program

Program ini merupakan pengembangan dari Posttest 1 dengan tema **Sistem Pengelolaan Penjualan Produk Skincare**. Program digunakan untuk mengelola data produk, pelanggan, dan penjualan.

Pada Posttest 2, program dikembangkan dengan menerapkan konsep **Relasi UML** yang terdiri dari Asosiasi, Agregasi, dan Komposisi. Selain itu, program juga menerapkan konsep **Inheritance** yang terdiri dari superclass, subclass, `super()`, atribut tambahan, method overriding, serta penggunaan akses Protected dan Private.

---

## 2. Tujuan

Tujuan dari program ini adalah untuk menerapkan konsep Object Oriented Programming (OOP), khususnya Relasi UML dan Inheritance dalam sebuah sistem pengelolaan penjualan produk skincare.

Program ini juga bertujuan agar data produk, pelanggan, dan transaksi dapat dikelola menggunakan konsep class dan object dengan menerapkan encapsulation, property, class method, static method, serta validasi data.

---

## 3. Class yang Digunakan

Program terdiri dari beberapa class, yaitu:

### 3.1 Class Produk

Class `Produk` digunakan untuk menyimpan data produk skincare.

Atribut yang digunakan antara lain:

* `nama`
* `harga`
* `__stok`

Class ini juga memiliki class attribute seperti `nama_toko`, `jenis_toko`, dan `jumlah_produk`.

---

### 3.2 Class Pelanggan

Class `Pelanggan` merupakan **Superclass** yang digunakan sebagai dasar untuk membuat jenis pelanggan.

Atribut yang digunakan:

* `_nama` sebagai Protected Attribute
* `_alamat` sebagai Protected Attribute
* `__saldo` sebagai Private Attribute

Class ini memiliki method `tampilkan()`, property `saldo`, class method `tampilkan_total()`, dan static method `cek_nama()`.

---

### 3.3 Class PelangganMember

Class `PelangganMember` merupakan **Subclass** dari class `Pelanggan`.

Class ini menggunakan:

```python
super().__init__(nama, alamat, saldo)
```

Atribut khusus yang dimiliki adalah:

```python
self.diskon_member
```

Method `tampilkan()` juga melakukan **method overriding** dari superclass `Pelanggan`.

---

### 3.4 Class PelangganNonMember

Class `PelangganNonMember` merupakan **Subclass** kedua dari class `Pelanggan`.

Class ini menggunakan:

```python
super().__init__(nama, alamat, saldo)
```

Atribut khusus yang dimiliki adalah:

```python
self.biaya_admin
```

Class ini juga melakukan overriding terhadap method `tampilkan()`.

---

### 3.5 Class DetailPenjualan

Class `DetailPenjualan` digunakan untuk menyimpan detail dari suatu transaksi, yaitu nama produk dan jumlah produk.

Class ini digunakan sebagai bagian dari **relasi Komposisi** dengan class `Penjualan`.

---

### 3.6 Class Penjualan

Class `Penjualan` digunakan untuk mengelola transaksi antara pelanggan dan produk.

Atribut yang digunakan antara lain:

* `pelanggan`
* `produk`
* `jumlah`
* `__total`
* `detail`

Class ini juga memiliki property `total`, class method `ubah_pajak()`, dan static method `hitung_diskon()`.

---

# 4. Penerapan Relasi UML

Program menerapkan tiga jenis relasi UML yang diminta.

## 4.1 Asosiasi

Asosiasi terjadi antara class `Penjualan` dan `Pelanggan`.

Pada class `Penjualan` terdapat:

```python
self.pelanggan = pelanggan
```

Artinya objek `Penjualan` berhubungan dengan objek `Pelanggan`. Pelanggan melakukan transaksi melalui objek Penjualan.

Contoh:

```python
penjualan1 = Penjualan(
    pelanggan1,
    produk1,
    2
)
```

Pada contoh tersebut, `pelanggan1` dihubungkan dengan `penjualan1`.

---

## 4.2 Agregasi

Agregasi terjadi antara class `Penjualan` dan class `Produk`.

Pada class `Penjualan` terdapat:

```python
self.produk = produk
```

Objek `Produk` dibuat terlebih dahulu di luar class `Penjualan`.

Contohnya:

```python
produk1 = Produk("Facial Wash", 35000, 10)
```

Kemudian produk tersebut digunakan dalam transaksi:

```python
penjualan1 = Penjualan(
    pelanggan1,
    produk1,
    2
)
```

Hal ini menunjukkan bahwa objek `Produk` dapat berdiri sendiri dan tidak bergantung pada objek `Penjualan`.

---

## 4.3 Komposisi

Komposisi terjadi antara class `Penjualan` dan `DetailPenjualan`.

Pada class `Penjualan` terdapat:

```python
self.detail = DetailPenjualan(produk.nama, jumlah)
```

Objek `DetailPenjualan` dibuat langsung di dalam class `Penjualan`.

Dengan demikian, `DetailPenjualan` menjadi bagian dari `Penjualan` dan keberadaannya bergantung pada transaksi tersebut.

---

# 5. Penerapan Inheritance

Program menerapkan inheritance dengan menggunakan satu superclass dan dua subclass.

Struktur inheritance:

```text
              Pelanggan
              /       \
             /         \
PelangganMember     PelangganNonMember
```

## 5.1 Superclass

Superclass yang digunakan adalah:

```python
class Pelanggan:
```

Class ini memiliki atribut dan method dasar yang dapat diwariskan kepada subclass.

---

## 5.2 Subclass

Subclass yang digunakan adalah:

```python
class PelangganMember(Pelanggan):
```

dan:

```python
class PelangganNonMember(Pelanggan):
```

Kedua subclass tersebut mewarisi atribut dan method dari class `Pelanggan`.

---

# 6. Penggunaan super()

Kedua subclass memanggil konstruktor dari superclass menggunakan `super()`.

Pada `PelangganMember`:

```python
super().__init__(nama, alamat, saldo)
```

Pada `PelangganNonMember`:

```python
super().__init__(nama, alamat, saldo)
```

Penggunaan `super()` memungkinkan subclass menggunakan konstruktor yang sudah dibuat pada superclass.

---

# 7. Atribut Tambahan pada Subclass

Setiap subclass memiliki atribut khusus yang membedakannya.

### PelangganMember

Memiliki atribut:

```python
self.diskon_member = diskon_member
```

Atribut tersebut digunakan untuk menyimpan persentase diskon khusus pelanggan member.

### PelangganNonMember

Memiliki atribut:

```python
self.biaya_admin = biaya_admin
```

Atribut tersebut digunakan untuk menyimpan biaya administrasi pelanggan non-member.

---

# 8. Method Overriding

Method `tampilkan()` yang terdapat pada superclass `Pelanggan` di-override pada kedua subclass.

Superclass:

```python
def tampilkan(self):
    print("Nama   :", self._nama)
    print("Alamat :", self._alamat)
    print("Saldo  : Rp", self.__saldo)
```

Pada `PelangganMember`, method tersebut dibuat kembali untuk menampilkan status member dan diskon.

Pada `PelangganNonMember`, method tersebut dibuat kembali untuk menampilkan status non-member dan biaya administrasi.

Dengan demikian, setiap subclass memiliki perilaku `tampilkan()` yang berbeda.

---

# 9. Protected dan Private

Program menggunakan dua tingkat akses yang diminta.

## Protected

Atribut Protected digunakan pada:

```python
self._nama
self._alamat
```

Atribut tersebut menggunakan satu garis bawah `_` dan dapat diakses oleh subclass.

Contohnya pada `PelangganMember`:

```python
print("Nama   :", self._nama)
```

---

## Private

Atribut Private digunakan pada:

```python
self.__saldo
```

Atribut tersebut menggunakan dua garis bawah `__` sehingga hanya digunakan secara langsung di dalam class `Pelanggan`.

Akses terhadap saldo dilakukan menggunakan property:

```python
@property
def saldo(self):
    return self.__saldo
```

dan setter:

```python
@saldo.setter
def saldo(self, nilai):
    if nilai < 0:
        raise ValueError("Saldo tidak boleh negatif!")

    self.__saldo = nilai
```

---

# 10. Encapsulation dan Property

Program juga menerapkan encapsulation pada data stok, saldo, dan total penjualan.

Contohnya pada stok:

```python
@property
def stok(self):
    return self.__stok
```

Setter digunakan untuk melakukan validasi:

```python
@stok.setter
def stok(self, nilai):
    if nilai < 0:
        raise ValueError("Stok tidak boleh negatif!")
    self.__stok = nilai
```

Dengan adanya setter, nilai stok tidak dapat diberikan angka negatif.

Hal yang sama diterapkan pada `saldo` dan `total`.

---

# 11. Class Method

Program menggunakan beberapa class method.

Contohnya:

```python
@classmethod
def ganti_nama_toko(cls, nama):
```

Method tersebut digunakan untuk mengubah nama toko.

Class method lainnya adalah:

```python
Pelanggan.tampilkan_total()
```

dan:

```python
Penjualan.ubah_pajak(0.11)
```

---

# 12. Static Method

Program menggunakan static method untuk proses yang tidak bergantung pada object tertentu.

Contohnya:

```python
@staticmethod
def cek_harga(harga):
    return harga > 0
```

Static method lainnya digunakan untuk mengecek nama dan menghitung diskon.

---

# 13. Pengujian Program

Program diuji menggunakan beberapa data.

### Data Produk

```text
Produk 1 : Facial Wash
Harga    : Rp35000
Stok     : 10

Produk 2 : Moisturizer
Harga    : Rp50000
Stok     : 15
```

Stok produk pertama kemudian diubah menjadi 20.

Program juga menguji validasi stok dengan memberikan nilai `-5`. Program menampilkan pesan:

```text
Validasi: Stok tidak boleh negatif!
```

---

### Data Pelanggan

Pelanggan yang digunakan:

```text
Dava
Status : Member
Diskon : 10%

Meyssa
Status : Non Member
Biaya Admin : Rp5000
```

Saldo Dava juga diuji dengan perubahan saldo dari Rp100.000 menjadi Rp200.000.

Program kemudian menguji saldo negatif dan menampilkan:

```text
Validasi: Saldo tidak boleh negatif!
```

---

### Data Penjualan

Transaksi pertama:

```text
Pelanggan : Dava
Produk    : Facial Wash
Jumlah    : 2
Total     : Rp70000
```

Transaksi kedua:

```text
Pelanggan : Meyssa
Produk    : Moisturizer
Jumlah    : 3
Total     : Rp150000
```

---

# 14. Pengujian Relasi UML

Program menampilkan penerapan ketiga relasi UML.

```text
--- RELASI UML ---

Asosiasi:
Pelanggan Dava melakukan transaksi dengan Penjualan.

Agregasi:
Penjualan menggunakan Produk: Facial Wash

Komposisi:
Penjualan memiliki DetailPenjualan:
Produk : Facial Wash
Jumlah : 2
```

Hasil tersebut menunjukkan bahwa ketiga relasi UML telah diterapkan dalam program.

---

# 15. Pengujian Inheritance

Inheritance diuji dengan membuat objek:

```python
pelanggan1 = PelangganMember(
    "Dava",
    "Balikpapan",
    100000,
    10
)
```

dan:

```python
pelanggan2 = PelangganNonMember(
    "Meyssa",
    "Samarinda",
    150000,
    5000
)
```

Kedua objek tersebut mewarisi konstruktor dari `Pelanggan` menggunakan `super()` dan memiliki atribut khusus masing-masing.

Method `tampilkan()` juga menghasilkan tampilan yang berbeda sesuai dengan jenis pelanggan.

---

# 16. Kesimpulan

Program **Sistem Pengelolaan Penjualan Produk Skincare** telah dikembangkan dengan menerapkan konsep OOP pada Posttest 2. Program sudah menerapkan tiga Relasi UML, yaitu **Asosiasi, Agregasi, dan Komposisi**.

Selain itu, program juga menerapkan **Inheritance** dengan satu superclass yaitu `Pelanggan` dan dua subclass yaitu `PelangganMember` dan `PelangganNonMember`. Penggunaan `super()`, atribut tambahan pada subclass, method overriding, Protected Attribute, dan Private Attribute juga telah diterapkan.

Dengan penerapan tersebut, program dapat menunjukkan penggunaan konsep OOP secara lebih terstruktur dalam sistem pengelolaan produk, pelanggan, dan transaksi penjualan skincare.
