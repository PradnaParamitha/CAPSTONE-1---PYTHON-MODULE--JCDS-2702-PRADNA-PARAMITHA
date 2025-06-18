# README PROGRAM PENJUALAN BARANG TOKO SEDERHANA DENGAN PYTHON

Program dalam repository ini yang berjudul “Program Penjualan Barang Toko” berisi kode dalam format python yang dibuat untuk memenuhi tugas Capstone Purwadhika untuk kelas JCDS-2072. Program Penjualan Barang Toko ini berfungsi untuk membantu pegawai toko fiksional bernama Toko Kelontong Kami untuk melihat serta mencatat inventori barang serta melakukan jual beli dengan fungsi kasir yang terdapat dalam program.

  

Program ini ditujukan untuk membantu pengguna program untuk mengecek inventori barang toko; menambahkan, menghapus, serta mengedit data barang,; dan melakukan penghitungan jual-beli barang.


## **Fitur Utama**

##### 1.  Login Karyawan
    

  

Untuk menjaga keamanan barang, karyawan melakukan login terlebih dahulu sebelum mengakses dan menggunakan program ini. Adapun data yang perlu diisi antara lain Nama, ID Karyawan serta Password (data dummy akan diberikan di bawah).

  

##### 2.  Menampilkan Daftar Barang
    

Fitur ini berfungsi untuk menampilkan kode, nama, stok dan harga barang yang telah tersedia. Sebagai placeholder, saya telah menyiapkan tiga item (Sabun, Tisu, Odol) dalam rangkaian data dummy.

  

Fitur ini merupakan salah satu fitur yang berfungsi memenuhi kebutuhan fitur READ yang terdapat dalam ketentuan Capstone.

##### 3.  Menambah Barang Baru
    

Fitur ini berfungsi untuk menambah item baru ke dalam inventori dengan penambahan kode secara otomatis. Fitur ini merupakan salah satu fitur yang berfungsi memenuhi kebutuhan fitur CREATE yang terdapat dalam ketentuan Capstone.

  

##### 4.  Menghapus Barang
    

  

Fitur ini berfungsi untuk menghapus item dari daftar barang. Dalam hal ini, penghapusan dilakukan berdasarkan kode barang (tiap kode barang bersifat unik atau di-assign ke masing-masing barang. Fitur ini merupakan fitur yang berfungsi memenuhi kebutuhan fitur DELETE yang terdapat dalam ketentuan Capstone.

  

##### 5.  Mengedit Data Barang
    

Fitur ini dikembangkan sebagai fitur tambahan setelah fungsi untuk menambah dan menghapus data barang. Pengguna program, seperti di menu menghapus barang, dapat mengedit data barang (nama, stok, harga) berdasarkan kode barang tertentu.

  

Fitur ini merupakan salah satu fitur yang berfungsi memenuhi kebutuhan fitur UPDATE untuk memperbarui data barang yang terdapat dalam ketentuan Capstone.

  

##### 6.  Membeli Barang (Cart & Checkout)
    

  

Dalam program penjualan barang toko, fungsi untuk membeli barang sangatlah dibutuhkan. Karena itu, saya menambahkan menu kasir agar pengguna aplikasi dapat menambah barang ke cart dan melakukan checkout saat ada pelanggan yang ingin membeli barang. Menu kasir ini dapat melakukan antara lain menambahkan barang ke keranjang, menghitung subtotal, input uang pembayaran, dan menghitung kembalian.

  

Fitur ini merupakan salah satu fitur yang dapat memenuhi kebutuhan fitur UPDATE yang terdapat dalam ketentuan Capstone karena berfungsi memperbarui stok barang dengan cara mengurangi stok setelah pembelian barang

  

##### 7.  Keluar Program
    

  

Menu ini menyediakan opsi keluar dari program dengan konfirmasi pengguna.

  



## **Flow Penggunaan Program**

Berikut adalah flow “Program Penjualan Barang Toko” dari awal hingga akhir

  

#### 1.  Inisiasi program
    

  

Tampilkan salam pembuka dan minta login karyawan:

-   Nama (unik), tidak case-sensitive
    
-   ID Karyawan (unik)
    
-   Password
    

  

#### 2.  Validasi Login
    

  

Jika:

-   Berhasil → lanjut ke menu utama  
      
    
-   Gagal → ulangi input sampai benar
    

  

#### 3.  Menu Utama
    

  

1. Menampilkan Daftar Barang

2. Menambah Barang

3. Menghapus Barang

4. Mengedit Data Barang

5. Membeli Barang

6. Keluar Program

  

#### Penjelasan menu

  

#### 3.1. Menampilkan Daftar Barang (READ)

3.1.1. Menampilkan tabel:

-   Kode
    
-   Nama Barang
    
-   Stok
    
-   Harga
    

  

3.1.2. Keluar ke menu utama:

-   User mengetik 0
    

  

#### 3.2. Menambah Barang (CREATE)

3.2.1. Menampilkan tabel barang berdasarkan update terakhir

3.2.2. Input:

-   Nama barang baru
    
-   Stok
    
-   Harga
    

  

3.2.3. Menambah kode secara otomatis dari kode terakhir

3.2.4. Barang baru ditambahkan ke list dan update inventori

-   Menampilkan tabel inventori yang sudah ditambahkan barang baru
    

3.2.4. Konfirmasi menambah barang baru atau tidak

-   Ya: mengulangi proses dari 3.2.1
    
-   Tidak: Keluar ke menu utama
    

#### 3.3. Menghapus Barang (DELETE)

3.3.1. Menampilkan tabel barang berdasarkan update terakhir

3.3.2 . Input:

-   Kode barang yang ingin dihapus
    

3.3.3. Barang dihapus dari list dan update inventori

-   Menampilkan tabel inventori yang sudah dikurangi barangnya
    

3.3.4. Konfirmasi menambah barang lain atau tidak

-   Ya: mengulangi proses dari 3.3.1
    
-   Tidak: Keluar ke menu utama
    

  

#### 3.4. Mengedit Data Barang (UPDATE)

3.4.1. Menampilkan tabel barang berdasarkan update terakhir

3.4.2. Menu untuk memilih data barang yang ingin diedit (selain kode):

1.  Mengubah nama barang
    
2.  Mengubah stok barang
    
3.  Mengubah harga barang
    

3.4.3. Memasukkan angka menu yang ingin dijalankan

-   Mengganti konten data:
    

1.  Nama barang
    
2.  Stok barang
    
3.  Harga barang
    

3.4.4. Update data barang berdasarkan input pengguna

-   Pemberian kode secara otomatis berdasarkan angka kode terakhir
    
-   Menampilkan tabel inventori yang datanya sudah update
    

3.4.5.. Konfirmasi mengedit barang lain atau tidak

-   Ya: mengulangi proses dari 3.4.1
    
-   Tidak: Keluar ke menu utama
    

  
  

#### 3.5. Membeli barang (UPDATE)

3.5.1. Menampilkan tabel barang berisi nama, ketersediaan (stok dan harga barang yang bisa dibeli

3.5.1. Memasukkan barang ke dalam cart:

1.  Memilih kode barang yang akan dimasukkan dalam cart
    
2.  Memasukkan jumlah barang yang akan dibeli
    

-   Kode mengurangi stok berdasarkan jumlah barang yang dibeli
    

 3.5.2. Konfirmasi membeli barang lain atau tidak

-   Ya: mengulangi proses 3.5.1
    
-   Tidak: Keluar ke menu utama
    

3.5.3. Memasukkan angka menu yang ingin dijalankan

-   Mengganti konten data:
    

4.  Nama barang
    
5.  Stok barang
    
6.  Harga barang
    

3.5.4. Update data barang berdasarkan input pengguna

-   Pemberian kode secara otomatis berdasarkan angka kode terakhir
    
-   Menampilkan tabel inventori yang datanya sudah update
    

3.5.5. Konfirmasi mengedit barang lain atau tidak

-   Ya: mengulangi proses 3.4
    
-   Tidak: Meneruskan proses pembayaran
    

3.5.6. Menampilkan barang belanjaan (cart)

3.5.7. Menampilkan total harga

3.5.8. Input jumlah uang dari pembeli

-   Kurang: Pengguna diminta memasukkan nominal lain hingga pas atau lebih
    
-   Pas : Pemberitahuan jumlah uang sudah pas dan ucapan terima kasih
    
-   Lebih : Menghitung dan menampilkan jumlah uang kembalian dan ucapan terima kasih
    

  

#### 3.6. Keluar Program

3.6.1 Meminta konfirmasi apakah pengguna ingin keluar

-   Ya : Menampilkan ucapan terima kasih dan program selesai
    

- Tidak : Kembali ke menu utama

## **Struktur Data**

Kode ini menggunakan beberapa list utama yang digunakan untuk menyimpan informasi inventori.

| Variabel | Deskripsi                                | Isi List                     | Tipe Data |
|----------|-------------------------------------------|------------------------------|-----------|
| kode     | List kode unik barang (angka)             | 1001, 1002, 1003             | Integer   |
| barang   | List nama barang                          | 'Sabun', 'Tisu', 'Odol'      | String    |
| stok     | List jumlah stok masing-masing barang     | 30, 20, 20                   | Integer   |
| harga    | List harga satuan masing-masing barang    | 5000, 10000, 15000           | Integer   |

## **Dummy Data**

Berikut adalah data dummy karyawan  yang telah disiapkan sebelumnya untuk login program.

| Nama  | ID Karyawan | Password    |
|-------|-------------|-------------|
| Alice | AL01        | welcome123  |
| Budi  | BU02        | welcome123  |
| Cece  | CE03        | welcome123  |

## Informasi Penulis

Program ini dibuat oleh Pradna Aqmaril Paramitha sebagai bagian dari pembelajaran Capstone Modul 1: Python, kelas JCDS-2702 - Purwadhika BSD.


## Lisensi

Program ini bebas digunakan dan dimodifikasi untuk keperluan edukasi atau non-komersial lainnya.

