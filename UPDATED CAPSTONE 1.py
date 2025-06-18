kode = [1001,1002,1003]
kode_akhir = 1003
barang = ['Sabun', 'Tisu', 'Odol']
stok = [30, 20, 20]
harga = [5000, 10000, 15000]

nama = ['Alice', 'Budi', 'Cece']
user_id = ['AL01', 'BU02', 'CE03']
password = 'welcome123'

def salam_booting():
  print('''Selamat Datang di Toko Kelontong Kami!
Silakan masukkan Nama, Kode ID, dan Password Anda:''')
  while True:
    print ("Masukkan Data Login Anda")
    input_nama = input(f"Nama:")
    input_id = input("Nomor ID: ")
    input_pass = input("Password: ")

    if input_nama.capitalize() in nama:
      index_user = nama.index(input_nama.capitalize())
      if input_id == user_id[index_user] and input_pass == password:
        print(f"Halo {input_nama}, selamat datang di Program Kasir dan Inventori Toko Kelontong Kami!")
        return input_nama 
      else:
        print("ID atau password tidak sesuai.")
    else:
      print("Nama tidak ditemukan. Silakan coba lagi.")

def menu_barang():
  print ("\nDaftar barang\n")
  print ( "Kode \t| Nama   \t| Stok \t| Harga ")
  for i in range(len(barang)):
    print (f"{kode[i]}  \t| {barang[i]}  \t| {stok[i]}  \t| {harga[i]}")

input_nama = salam_booting() 

cart = []
while True :
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

  if input_menu == '1':
    while True:
      def tampil_menu():
        menu_barang()

      tampil_menu()
      menu_keluar = input ('''
Ketik '0' untuk keluar:''')
      if menu_keluar == '0':
        break
      else:
        print ("Maaf, mohon input angka yang lain.")

  elif (input_menu == '2'):
    while True:
      print ('''
Berikut inventori barang saat ini:''') 
      menu_barang()
      def tambah_barang():
        global kode_akhir
        barang_baru = (input(f"Masukkan nama barang baru yang ingin dimasukkan:"))
        stok_baru = int(input(f"Masukkan stok barang baru yang ingin dimasukkan:"))
        harga_baru = int(input(f"Masukkan harga barang baru yang ingin dimasukkan:"))

        barang_baru = barang_baru.title()

        kode_akhir +=1
        kode.append(kode_akhir)
        barang.append(barang_baru)
        stok.append(stok_baru)
        harga.append(harga_baru)

      tambah_barang()
      print ('''
Berikut inventori barang terbaru:''')
      menu_barang()

      add_confirm = input("Mau menambahkan barang yang lain? (ya/tidak): ").lower()
      if add_confirm.lower() == "tidak":
        break
      elif add_confirm.lower() == "ya":
        continue
      else:
        print ("Maaf, mohon input perintah yang lain.")

  elif (input_menu == '3'):
    while True:
      print ('''
Berikut inventori barang saat ini:''')
      menu_barang()
      def hapus_barang():
        kode_hapus= int(input(f"Masukkan kode barang yang ingin dihapus:"))
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
Berikut inventori barang terbaru:''')
      menu_barang()
      delete_confirm = input("Mau menghapus barang yang lain? (ya/tidak): ").lower()
      if delete_confirm.lower() == "tidak":
        break
      elif delete_confirm.lower()== "ya":
        continue
      else:
        print ("Maaf, mohon input angka yang lain.")

  elif (input_menu == '4'):
    while True:
      print ('''
Berikut inventori barang saat ini:''')
      menu_barang()
      def edit_barang():
        kode_edit= int(input(f"Masukkan kode barang yang ingin diedit:"))
        if kode_edit in kode:
          index = kode.index(kode_edit)
          input_edit = input ('''

Bagian apa yang ingin Anda edit?

1. Mengubah nama barang
2. Mengubah stok barang
3. Mengubah harga barang

* Angka kode tidak dapat diedit

Masukkan angka Menu yang ingin dijalankan : ''')
          if input_edit == '1':
            barang[index] = str(input(f"Masukkan nama barang baru:"))
          elif input_edit == '2':
            stok[index] = int(input(f"Masukkan jumlah stok baru:"))
          elif input_edit == '3':
            harga[index] = int(input(f"Masukkan harga barang baru:"))
          else:
            print ("Maaf, kode menu yang Anda masukkan tidak ditemukan. Mohon pilih angka lain")

          print ('''
Berikut inventori barang terbaru:''')
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
      edit_confirm = input("Mau mengedit barang yang lain? (ya/tidak): ").lower() 
      if edit_confirm.lower() == "tidak":
        break
      elif edit_confirm.lower() == "ya":
        continue
      else:
        print ("Maaf, mohon input perintah yang lain.")

  elif (input_menu == '5'):
    while True:
      cart = []
      def menu_cart(cart):
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

        kode_cart= int(input("Masukkan kode barang yang ingin dibeli: "))
        if kode_cart not in kode:
          print ("Kode barang tidak ditemukan.")
          continue
        stok_cart = int(input("Masukkan stok barang yang ingin dibeli: "))
        index_cart = kode.index(kode_cart)
        if stok_cart > stok[index_cart]:
          print(f"Stock tidak cukup, stock {barang[index_cart]} tinggal {stok[index_cart]}")
          continue
        cart.append ((index_cart, stok_cart))
        stok [index_cart] -= stok_cart

        print ("Berikut isi keranjang Anda:\n")
        subtotal = menu_cart(cart) 

        cart_confirm = input("Mau beli yang lain? (ya/tidak): ").lower()
        if cart_confirm == "ya":
          continue
        elif cart_confirm == "tidak":
          print ("Berikut total belanjaannya:\n")
          subtotal = menu_cart(cart) 
          while True:
            uang_masuk = int(input(f"Masukkan jumlah uang Anda:"))
            if uang_masuk < subtotal:
              print ("Maaf, uang Anda tidak cukup.")
            elif uang_masuk == subtotal:
              print ("Uang yang dimasukkan sudah pas. Terima kasih!")
              break
            elif uang_masuk >= subtotal:
              uang_kembali = uang_masuk - subtotal
              print ("Terima kasih. Kembaliannya sejumlah", uang_kembali)
              break
          break 

  elif (input_menu == '6'):
    exit_confirm = input("Apakah Anda yakin ingin keluar dari program ini? (ya/tidak): ").lower()
    if exit_confirm.lower() == "ya":
      print(f"Terima kasih {input_nama}, telah menggunakan program kami!") 
      break
    elif exit_confirm.lower() == "tidak":
      continue
    else:
      print ("Maaf, mohon input perintah yang lain.")
  else:
    print ("Maaf, angka yang Anda masukkan tidak ditemukan dalam list menu.")
