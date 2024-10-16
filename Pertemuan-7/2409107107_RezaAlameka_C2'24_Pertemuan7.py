# # Membuat Fungsi
# def salam():
#     print ("Selamat Pagi, FT Muda")
# def kali():
#     x = 6*4
#     print(x)
# # Pemanggilan Fungsi
# salam()
# kali()
# # Hasilnya:
# # Selamat Pagi, FT Muda
# # 24
# # Pemanggilan Fungsi 3 kali
# salam()
# salam()
# salam()
# kali()
# kali()
# kali()


# # Membuat fungsi dengan parameter (panjang, lebar)
# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print ("Luas persegi panjang:", luas)
# # Pemanggilan fungsi luas_persegi_panjang
# luas_persegi_panjang(4, 6)


# Contoh Program mengembalikan hasil fungsi
# def luas_persegi(sisi):
#     luas = sisi * sisi
#     return luas
# print ("Luas persegi :", luas_persegi(8))

# def nilai(angka):
#     if angka >10 :
#         print("1")
#         return
#     else:
#         print("2")
#         return
#     print("3")

# def mhs(nama1,nama2,nama3):
#     print(nama3)

# mhs(nama3="reja",nama2="alam",nama1="eka")




import os
data_mahasiswa =[
    {
        "Nama" : "Andi",
        "Nim" : "123"
    },
    {
        "Nama" : "Budi",
        "Nim" : "124"
    },
    {
        "Nama" : "Ucup",
        "Nim" : "125"
    }
]
os.system('cls || clear')



while True:
    print("""
    Menu
Lihat Data  >> 1
Tambah Data >> 2
Edit Data   >> 3
Hapus Data  >> 4
Keluar      >> 5
""")
    pilih = input("Masukan Pilihan menu >> ")
    os.system('cls || clear')
    match(pilih):
        case "1":
            print("===Lihat Data===")
            for i in range(len(data_mahasiswa)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_mahasiswa[i]['Nama']}")
                print(f"Nim : {data_mahasiswa[i]['Nim']}")
                print("="*10)
            input("Enter.....")
            os.system('cls || clear')
        case "2":
            print("== Tambah Data ==")
            print("=" * 10)
            input_nama = input("Nama\t: ")
            input_nim = input("Nim\t: ")
            data_mahasiswa.append({
                "Nama" : input_nama,
                "Nim" : input_nim
            })
            print(f"{input_nama} dengan NIM {input_nim} telah ditambahkan")
            input("Enter....")
            os.system('cls || clear')
        case "3":
            print("== Ubah Data ==")
            for i in range(len(data_mahasiswa)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_mahasiswa[i]['Nama']}")
                print(f"Nim : {data_mahasiswa[i]['Nim']}")
                print("="*10)
            index= int(input("masukkan index yang mau diedit : "))
            if index > len(data_mahasiswa) or index < 0:
                print("Index tidak ditemukan")
                input("Enter.....")
                os.system('cls || clear')
            else:
                nama_baru = input("masukkan nama anda :")
                nim_baru = input("masukkan nim anda :")
                data_mahasiswa[index-1]["Nama"] = nama_baru
                data_mahasiswa[index-1]["Nim"] = nim_baru
                print("data berhasil diubah")
                input("Enter.....")
                os.system('cls || clear')
        case "4":
            print("== Hapus Data ==")
            for i in range(len(data_mahasiswa)):
                print(f"data ke {i+1}")
                print(f"Nama : {data_mahasiswa[i]['Nama']}")
                print(f"Nim : {data_mahasiswa[i]['Nim']}")
                print("="*10)
            index = int(input("masukkan index yang ingin dihapus: "))
            if index > len(data_mahasiswa) or index < 0:
                print("Index tidak ditemukan")
                input("Enter.....")
                os.system('cls || clear')
            else:
                del_data = data_mahasiswa.pop(index-1)
                print(f"{del_data['Nama']} dengan NIM {del_data['Nim']} telah dihapus")
                input("Enter......")
                os.system('cls || clear')
        case "5":
            print("Bye bye")
            exit()
        case _:
            print(f"Menu {pilih} tidak tersedia")
            input("Enter.....")
            os.system('cls || clear')
