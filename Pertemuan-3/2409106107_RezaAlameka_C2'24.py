# cuaca = str(input("Masukan Jenis cuaca:"))
# if cuaca == "cerah":
#     print("Kamu pergi keluar rumah")
# elif cuaca == "hujan":
#     print("Diam di rumah")
# elif cuaca == "mendung":
#     print("Hati-Hati")
# else :
#     print("Tolong masukan lagi")
# Umur = int(input("Masukkan umur Anda : "))
# if Umur <= 10:
#     print( "Umur Anda termasuk kategori anak-anak")
# elif Umur <= 18:
#     print("Umur Anda termasuk kategori remaja")
# elif Umur <=35:
#     print("Umur Anda termasuk kategori dewasa")
# elif Umur <=65:
#     print("Umur Anda termasuk kategori paruh baya")
# else:
#     print("Umur Anda termasuk kategori Tua")
# angka = int(input("Masukkan angka: "))
nim = int(input("Masukkan nim:"))
if nim >= 1 and nim <= 50 :
    if nim >= 1 and nim <= 25:
        print("Kelas A'1")
    else:
        print("kelas A'2")
elif nim >= 51 and nim <= 100:
    if nim >= 51 and nim <= 100:
        print("Kelas B'1")
    else:
        print("kelas B'2")
elif nim >= 101 and nim <= 121:
    if nim >= 101 and nim <= 110:
        print("kelas C'1")
    else:
        print("kelasC'2")
else:
        print("Anda bukan mahasiswa informatika 24")
    
# result = "Genap" if angka % 2 == 0 else "Ganjil"
# print(angka, "adalah angka",result)