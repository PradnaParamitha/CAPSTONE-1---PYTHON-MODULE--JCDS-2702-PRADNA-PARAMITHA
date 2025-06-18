kode = [1001,1002,1003]
kode_akhir = 1003
barang = ['Sabun', 'Tisu', 'Odol']
stok = [30, 20, 20]
harga = [5000, 10000, 15000]
# Serangkaian kode diatas berisi list barang, kode, jumlah stok serta harga. Saya memasukkan tiga barang dengan angka terakhir 1003. Saya menandai kode akhir agar nantinya bisa dilanjutkan jika ada penambahan barang baru

#sebelum program penjualan barang dapat diakses, saya membuat fitur login terlebih dahulu untuk karyawan toko yang ingin mengakses inventori barang. 
# Berikut adalah data dummy karyawan yang telah disiapkan sebelumnya untuk login program 
nama = ['Alice', 'Budi', 'Cece']
user_id = ['AL01', 'BU02', 'CE03']
password = 'welcome123'

# Untuk menjaga keamanan data barang, karyawan melakukan login terlebih dahulu sebelum mengakses dan menggunakan program ini. 
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
      if input_id == id[index_user] and input_pass == password:
          print(f"Halo {input_nama}, selamat datang di Program Kasir dan Inventori Toko Kelontong Kami!")
          return input_nama 
      else:
        print("ID atau password tidak sesuai.")
    else:
      print("Nama tidak ditemukan. Silakan coba lagi.")
#Saya membuat conditional dalam login dengan rinci untuk memastikan pengguna menginput data sesuai dengan nama dan kode unik karyawan yang telah disediakan 


def menu_barang():
  print ("\nDaftar barang\n")
  print ( "Kode \t| Nama   \t| Stok \t| Harga ")
  for i in range(len(barang)):
    print (f"{kode[i]}  \t| {barang[i]}  \t| {stok[i]}  \t| {harga[i]}")
#Saya membuat fungsi menu_barang terlebih dahulu karena akan digunakan secara berulang-ulang di sepanjang program


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
# Saat program berhasil akan ditampilkan sederet menu dan fungsi yang dapat dilakukan dalam program ini, berisi fungsi Create (Menambah Barang), Read (Menampilkan Daftar Barang),
# Update (Menambah, Mengedit Data Barang) dan Delete (Menghapus). Selain itu, terdapat juga fungsi jual-beli yang tidak termasuk dalam fungsi CRUD, namun tetap esensial untuk program penjualan barang toko
  if input_menu == '1': # Kode ini berfungsi untuk menampilkan barang (READ)
      while True:
        def view_menu():
          print ("\nDaftar barang\n")
          menu_barang()

        view_menu() # Call view_menu inside the loop
        menu_keluar = input ('''
Ketik '0' untuk keluar:''')
        if menu_keluar == '0':
            break
        else:
            print ("Maaf, mohon input angka yang lain.")

  elif (input_menu == '2'): # Kode ini berfungsi untuk menambah barang baru (fungsi Update) ke dalam inventori barang toko
    while True:
      print ('''
Berikut inventori barang saat ini:''')
      menu_barang()
      def tambah_barang():
        global kode_akhir #global ditambahkan ke variabel kode_akhir agar tetap dapat berlaku di luar fungsi berikut (karena sudah didefinisikan sebelumnya di luar fungsi):
        barang_baru = (input(f"Masukkan nama barang baru yang ingin dimasukkan:"))
        stok_baru = int(input(f"Masukkan stok barang baru yang ingin dimasukkan:"))
        harga_baru = int(input(f"Masukkan harga barang baru yang ingin dimasukkan:"))

        barang_baru = barang_baru.title() # Kode ini berfungsi untuk menyelaraskan format nama barang baru yang dimasukkan agar sesuai dengan format nama barang-barang sebelumnya

        kode_akhir +=1 #Kode ini digunakan untuk memberikan kode baru terhadap barang baru yang ditambahkan. Pemberian nomor kode diteruskan dari kode terakhir yang terdapat dalam daftar barang
        kode.append(kode_akhir)
        barang.append(barang_baru)
        stok.append(stok_baru)
        harga.append(harga_baru)


      tambah_barang()
      print ('''
Berikut inventori barang terbaru:''')
      menu_barang()
      #sebelum pengguna program beranjak ke fungsi lain yang terdapat dalam menu utama, menu Tambah Barang menanyakan apakah ada lagi barang lain yang ingin ditambahkan
      add_confirm = input("Mau menambahkan barang yang lain? (ya/tidak): ").lower()
      if add_confirm.lower() == "tidak":
        break
      elif add_confirm.lower() == "ya":
        continue
      else:
            print ("Maaf, mohon input perintah yang lain.")


  elif (input_menu == '3'): # Kode ini berfungsi untuk menghapus barang dari inventori barang toko (fungsi DELETE)
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



  elif (input_menu == '4'): # Kode untuk Membeli Barang ini merupakan fitur baru yang terdapat di luar fungsi CRUD, tetapi esensial dalam program Penjualan Barang Toko, yaitu fungsi untuk membeli barang yang mencakup menambahkan barang ke dalam cart, melakukan check out, dan input uang serta menghitung uang kembalian

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
            break 
          elif edit_confirm.lower() == "ya":
            continue
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
     cart = []
     # Terlebih dahulu, saya membuat fungsi yang menampilkan daftar barang yang dapat di-check out
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

        #dalam fungsi tersebut, setiap barang yang ditambah ke dalam keranjang akab dikurangi dari jumlah stok yang tersedia

        print ("Berikut isi keranjang Anda:\n")
        subtotal = menu_cart(cart) 

        cart_confirm = input("Mau beli yang lain? (ya/tidak): ").lower()
        if cart_confirm == "ya":
                continue
        elif cart_confirm == "tidak":
              print ("Berikut total belanjaannya:\n")
              subtotal = menu_cart(cart) 
        #Pada bagian ini, seluruh isi keranjang termasuk total harga ditampilkan
        # Kode selanjutnya membantu pengguna program menginput jumlah uang yang diserahkan oleh pelanggan untuk menghitung apakah uangnya kurang, pas atau jumlah kembaliannya
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
# Menu terakhir diinput apabila pengguna sudah selesai menggunakan program dan ingin keluar dari program
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
