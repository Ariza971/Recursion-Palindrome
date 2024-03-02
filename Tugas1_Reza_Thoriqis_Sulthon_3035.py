'''Recursion'''

m = int(input("Masukkan jumlah menu: "))
# Input berapa jumlah menu yang ingin dimasukkan
jumlah_menu = []
# Jumlah menu di simpan dalam list kosong
for i in range(m):
# Looping untuk setiap menu, berdasarkan jumlah menu yang diinputkan diatas yaitu (n)
  id_menu = i+1
  # digunakan untuk membuat id pada setiap menu
  parent_menu = int(input("Masukkan parent untuk menu ke-" + str(i + 1) + ": "))
  # input untuk setiap parent menu, sesuai jumlah menu
  label_menu = f"menu {i+1}"
  # Membuat label memu dengan format menu[nomor]
  jumlah_menu.append({"id": id_menu,"parent": parent_menu, "label": label_menu,})
  # Menambah dictionary ke dalam list Jumlah Menu, berisi id, parent, dan label

# fungsi akan Mencetak menu secara rekursif
def print_menu(jumlah_menu, parent_menu, indent):
  for x in jumlah_menu:
    if x["parent"] == parent_menu:
      # Memeriksa menu sesuai dengan parent berdasarkan parent_menu, apabila sama maka akan di cetak 
      print(".." * indent, end="")
      # Mencetak identasi sebanyak indent dan end="" untuk menghapus baris baru selanjutnya
      print(x["label"])
      # Mencetak label dari menu yang telah diproses
      print_menu(jumlah_menu, x["id"], indent + 2)
      # pemanggilan secara rekursif, sebagai menambahkan banyaknya identasi 

print_menu(jumlah_menu,0,0)
# pemanggilan pertama fungsi print_menu, dan dimulai dari parent menu 0

'''Palindrome'''

# def palindcheck(x):
#     '''Fungsi untuk memeriksa apakah sebuah kata palindrome'''
#     x = x.lower().replace(" ", "")
#     # kata yang diinputkan akan dijadikan lowercase dan dihapus spasi
#     if len(x) <= 1:
#         return True
#     # Base Case dari fungsi palindcheck
#     # jika kata yang diinputkan hanya 1 huruf maka return True, karena tidak ada kata pembanding
#     elif x[0] != x[-1]:
#         return False
#     # Membandingkan kata pertama dan kata terakhir (ujung awal dan akhir)
#     else :
#         return palindcheck(x[1:-1])
#     # Memanggil fungsi palindcheck lagi untuk melakukan recursion dari kata yang belum di cek
    
# input_kata = input("Masukkan kata: ")
# # Meminta input kata dari user
# if palindcheck(input_kata):
#     print(f"kata {input_kata} adalah Palindrome")
#     # jika kata yang di input user memenuhi kriteria palindrome, maka termasuk palindrome
# else:
#     print(f"kata {input_kata} Bukan palindrome")
#     # apabila kata yang di input user tidak memenuhi kriteria palindrome, maka Bukan palindrome