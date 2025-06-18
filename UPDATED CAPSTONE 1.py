# Kode ini menggunakan beberapa list utama yang berisi data dummy sebagai data awal (dapat ditambahkan dan dikurangi)
kode = [1001,1002,1003]
kode_akhir = 1003
barang = ['Sabun', 'Tisu', 'Odol']
stok = [30, 20, 20]
harga = [5000, 10000, 15000]
# Berikut adalah data dummy karyawan yang telah disiapkan sebelumnya untuk diinput saat login program 
nama = ['Alice', 'Budi', 'Cece']
user_id = ['AL01', 'BU02', 'CE03']
password = 'welcome123'
#Fungsi di bawah ini adalah fungsi yang pertama kali berjalan saat program diaktifkan
def salam_booting():
  print('''Selamat Datang di Toko Kelontong Kami!
Silakan masukkan Nama, Kode ID, dan Password Anda:''')
  while True:
    print ("Masukkan Data Login Anda")
    input_nama = input(f"Nama:")
    input_id = input("Nomor ID: ")
    input_pass = input("Password: ")
# Validasi login telah dibuat sedemikian rupa agar semua input yang dimasukkan ke dalam field login sudah sesuai
    if input_nama.capitalize() in nama:
      index_user = nama.index(input_nama.capitalize())
      if input_id == user_id[index_user] and input_pass == password:
        print(f"Halo {input_nama}, selamat datang di Program Kasir dan Inventori Toko Kelontong Kami!")
        return input_nama 
      else:
        print("ID atau password tidak sesuai.")
    else:
      print("Nama tidak ditemukan. Silakan coba lagi.")
#Fungsi menu_barang di bawah ini menampilkan barang sesuai data yang paling update. Kode ini penting untuk dijadikan fungsi karena merupakan salah satu kode yang paling sering digunakan berulang-ulang
def menu_barang():
  print ("\nDaftar barang\n")
  print ( "Kode \t| Nama   \t| Stok \t| Harga ")
  for i in range(len(barang)):
    print (f"{kode[i]}  \t| {barang[i]}  \t| {stok[i]}  \t| {harga[i]}")

input_nama = salam_booting() 

cart = []
while True :
  #Menampilkan menu utama setelah berhasil login
  input_menu = input ('''
  Selamat Datang di Toko Kelontong Kami!

  List Menu :
  1. Menampilkan Daftar Barang
  2. Menambah Barang
  3. Menghapus Barang
  4. Mengedit Data Barang
  5. Membeli Barang
  6. Keluar Program

Masukkan angka Menu yang ingin dijalankan : ''')

  if input_menu == '1': # Menampilkan Daftar Barang (READ). Fitur ini berfungsi untuk menampilkan kode, nama, stok dan harga barang yang telah tersedia.
    while True:
      def tampil_menu():
        menu_barang()

      tampil_menu()
      menu_keluar = input ('''
Ketik '0' untuk keluar:''') #Keluar ke Menu Utama
      if menu_keluar == '0':
        break
      else:
        print ("Maaf, mohon input angka yang lain.")

  elif (input_menu == '2'): # Menambah Barang (CREATE). Fitur ini berfungsi untuk menambah item baru ke dalam inventori dengan penambahan kode secara otomatis.
    while True:
      print ('''
Berikut inventori barang saat ini:''') # Menampilkan tabel barang berdasarkan update terakhir
      menu_barang()
      def tambah_barang(): # Fungsi untuk menampilkan tabel barang berdasarkan update terakhir
        global kode_akhir #Penambahan kode baru mengacu pada koe terakhir yang sudah dibuat di list yang tersedia
        barang_baru = (input(f"Masukkan nama barang baru yang ingin dimasukkan:"))
        stok_baru = int(input(f"Masukkan stok barang baru yang ingin dimasukkan:"))
        harga_baru = int(input(f"Masukkan harga barang baru yang ingin dimasukkan:"))
        #Pengguna dapat menginput nama, stok, serta harga barang baru
        barang_baru = barang_baru.title()

        kode_akhir +=1 # Menambah kode secara otomatis dari kode terakhir
        kode.append(kode_akhir)
        barang.append(barang_baru)
        stok.append(stok_baru)
        harga.append(harga_baru)

      tambah_barang()
      print ('''
Berikut inventori barang terbaru:''') # Menampilkan tabel inventori yang sudah ditambahkan barang baru
      menu_barang()

      add_confirm = input("Mau menambahkan barang yang lain? (ya/tidak): ").lower() # Konfirmasi menambah barang baru atau tidak
      if add_confirm.lower() == "tidak":
        break
      elif add_confirm.lower() == "ya":
        continue
      else:
        print ("Maaf, mohon input perintah yang lain.")

  elif (input_menu == '3'): #Menghapus Barang (DELETE). Fitur ini berfungsi untuk menghapus item dari daftar barang.
    while True:
      print ('''
Berikut inventori barang saat ini:''') # Menampilkan tabel barang berdasarkan update terakhir
      menu_barang()
      def hapus_barang():
        kode_hapus= int(input(f"Masukkan kode barang yang ingin dihapus:")) # Pengguna menghapus barang yang diinginkan dengan menginput kode unik
        if kode_hapus in kode:
          index_hapus = kode.index(kode_hapus)
          del kode [index_hapus]
          del barang [index_hapus]
          del stok [index_hapus]
          del harga [index_hapus]
          print ("Barang berhasil dihapus.")
        else:
          print ("Maaf, kode barang yang Anda masukkan tidak ditemukan.")

      hapus_barang() 
      print ('''
Berikut inventori barang terbaru:''') # Menampilkan tabel barang berdasarkan update terakhir (barang sudah dihapus)
      menu_barang()
      delete_confirm = input("Mau menghapus barang yang lain? (ya/tidak): ").lower() Konfirmasi menghapus barang lain atau tidak
      if delete_confirm.lower() == "tidak":
        break
      elif delete_confirm.lower()== "ya":
        continue
      else:
        print ("Maaf, mohon input angka yang lain.")

  elif (input_menu == '4'): #Mengedit Data Barang (UPDATE). Fitur ini dikembangkan sebagai fitur tambahan setelah fungsi untuk menambah dan menghapus data barang. 
    while True:
      print ('''
Berikut inventori barang saat ini:''') # Menampilkan tabel barang berdasarkan update terakhir
      menu_barang()
      def edit_barang():
        kode_edit= int(input(f"Masukkan kode barang yang ingin diedit:"))
        if kode_edit in kode:
          index = kode.index(kode_edit)
          input_edit = input ('''

Bagian apa yang ingin Anda edit? # Menu untuk memilih data barang yang ingin diedit (kecuali kode yang bersifat otomatis):

1. Mengubah nama barang
2. Mengubah stok barang
3. Mengubah harga barang

* Angka kode tidak dapat diedit

Masukkan angka Menu yang ingin dijalankan : ''') # Memasukkan angka menu yang ingin dijalankan
          if input_edit == '1': # Mengubah nama barang
            barang[index] = str(input(f"Masukkan nama barang baru:"))
          elif input_edit == '2': # Mengubah jumlah barang
            stok[index] = int(input(f"Masukkan jumlah stok baru:"))
          elif input_edit == '3': # Mengubah harga barang
            harga[index] = int(input(f"Masukkan harga barang baru:"))
          else:
            print ("Maaf, kode menu yang Anda masukkan tidak ditemukan. Mohon pilih angka lain")

          print ('''
Berikut inventori barang terbaru:''') #  Update data barang berdasarkan input pengguna
          menu_barang()

          edit_confirm = input("Mau mengedit barang yang lain? (ya/tidak): ").lower()
          if edit_confirm.lower() == "tidak":
            return
          elif edit_confirm.lower() == "ya":
            return
          else:
            print ("Maaf, mohon input perintah yang lain.")
        else:
          print ("Maaf, kode barang yang Anda masukkan tidak ditemukan. Masukkan kembali kode barang yang tersedia")
      edit_barang()
      edit_confirm = input("Mau mengedit barang yang lain? (ya/tidak): ").lower() # Konfirmasi mengedit barang lain atau tidak	
      if edit_confirm.lower() == "tidak":
        break
      elif edit_confirm.lower() == "ya":
        continue
      else:
        print ("Maaf, mohon input perintah yang lain.")

  elif (input_menu == '5'):# Membeli Barang (UPDATE). Pengguna aplikasi dapat menambah barang ke cart dan melakukan checkout saat ada pelanggan yang ingin membeli barang. Memenuhi fungsi UPDATE karena berfungsi memperbarui stok barang dengan cara mengurangi stok setelah pembelian barang
    while True:
      cart = []
      def menu_cart(cart): #Fungsi ini adalah program kasir yang menambahkan jumlah barang yang diminta pembeli ke dalam cart dan menghitungnya sesuai dengan harga dalam list barang yang terupdate.
        subtotal = 0
        print ( "Kode \t| Nama   \t| Jumlah \t| Subtotal ")
        for index, isicart in cart:
          sub = harga[index] * isicart
          subtotal = subtotal + sub
          print(f"{kode[index]} \t| {barang[index]} \t| {isicart} \t\t| {sub}")

        print(f"\nTotal belanja: Rp{subtotal}")
        return subtotal

      while True:
        print ("\nDaftar barang\n")
        menu_barang()
        # Memasukkan barang ke dalam cart:
        kode_cart= int(input("Masukkan kode barang yang ingin dibeli: ")) # Memilih kode barang yang akan dimasukkan dalam cart
        if kode_cart not in kode:
          print ("Kode barang tidak ditemukan.")
          continue
        stok_cart = int(input("Masukkan jumlah barang yang ingin dibeli: ")) # Memasukkan jumlah barang yang akan dibeli
        index_cart = kode.index(kode_cart)
        if stok_cart > stok[index_cart]:
          print(f"Stock tidak cukup, stock {barang[index_cart]} tinggal {stok[index_cart]}")
          continue
        cart.append ((index_cart, stok_cart))
        stok [index_cart] -= stok_cart # Mengurangi stok berdasarkan jumlah barang yang dibeli

        print ("Berikut isi keranjang Anda:\n")
        subtotal = menu_cart(cart) # Menampilkan barang belanjaan yang sudah dimasukkan dalam cart sejauh ini 

        cart_confirm = input("Mau beli yang lain? (ya/tidak): ").lower() # Konfirmasi mengedit barang lain atau tidak	
        if cart_confirm == "ya":
          continue
        elif cart_confirm == "tidak":
          print ("Berikut total belanjaannya:\n")
          subtotal = menu_cart(cart) # Menampilkan barang belanjaan saat ini beserta total harga barang yang dibeli (jumlah yang harus dibayar)
          while True:
            uang_masuk = int(input(f"Masukkan jumlah uang Anda:")) #  Input jumlah uang dari pembeli
            if uang_masuk < subtotal: # Pengguna diminta memasukkan nominal lain hingga pas atau lebih
              print ("Maaf, uang Anda tidak cukup.")
            elif uang_masuk == subtotal :# Pemberitahuan jumlah uang sudah pas dan ucapan terima kasih
              print ("Uang yang dimasukkan sudah pas. Terima kasih!")
              break
            elif uang_masuk >= subtotal:# Menghitung dan menampilkan jumlah uang kembalian dan ucapan terima kasih 
              uang_kembali = uang_masuk - subtotal
              print ("Terima kasih. Kembaliannya sejumlah", uang_kembali)
              break
          break 

  elif (input_menu == '6'):
    exit_confirm = input("Apakah Anda yakin ingin keluar dari program ini? (ya/tidak): ").lower() # Menghitung dan menampilkan jumlah uang kembalian dan ucapan terima kasih 
    if exit_confirm.lower() == "ya":
      print(f"Terima kasih {input_nama.capitalize()}, telah menggunakan program kami!") # Menampilkan ucapan terima kasih dan program selesai
      break
    elif exit_confirm.lower() == "tidak": # Kembali ke menu utama
      continue
    else:
      print ("Maaf, mohon input perintah yang lain.")
  else:
    print ("Maaf, angka yang Anda masukkan tidak ditemukan dalam list menu.")
