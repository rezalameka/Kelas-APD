# daftar_buku = {
#     "Buku1" : "Harry potter",
#     "Buku2" : "Twillight", 
#     "Buku3" : "Percy Jackson",
    
#     }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# Biodata = {
# "Nama" : "Aldy Ramadhan Syahputra",
# "NIM" : 2109106079,
# "KRS" : ["Program Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" :True,
# "Social Media" : {
# "Instagram" : "@aldyrmdhns_",
# "Discord" : "\'Izanami#6848"}}


# print(Biodata['Nama'],['Social Media'])

# print(f"nama saya adalah {Biodata['Nama']}")
# print(f"NIM Saya adalah {Biodata['NIM']}")
# print(f"Instagram : {Biodata['Social Media']['Instagram']}")


# games = dict(Sekiro = "Action", Pokemon = "Adventure",
# Valorant = "FPS")

# print(games["Sekiro"])

# Games = {
# "Games1" : "PUBG MOBILE",
# "Games2" : "Mobile Legend",
# "Games3" : {
#     "nama" : "COC",
#     "genre" : "Strategy"
# }

# }

# print((Games.get('Games3')).get('genre'))

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81,
# "Kimia" : 78,
# "Fisika" : 80
# }

# #tanpa menggunakan items
# for i in Nilai:
#     print(i)
# print("")

# #menggunakan items
# for i, j in Nilai.items():
#     print(f"Nilai {i} anda adalah {j}")



# Film = {
# "Avenger Endgame" : "Action",
# "Sherlock Holmes" : "Mystery",
# "The Conjuring" : "Horror"
# }
# Sebelum Ditambah

# print(Film)
# Film["Zombieland"] = "Comedy"
# Film.update({"Hours" : "Thriller"})


# #Setelah Ditambah

# print(Film)


#Penggunaan del:
# del Film["Avenger Endgame"]
# print(Film)

# simpan = Film.pop('Sherlock Holmes')
# print(Film)
# print(simpan)
# Film["Sherlock Holmes"] = simpan
# print(Film)


# Film.clear()
# print(Film)

# print("Jumlah Film = ",len


# movies = Film.copy()
# print(movies)


# key = "apel", "jeruk", "mangga"
# value = 1
# buah = dict.fromkeys(key, value)
# print(buah)


# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }
# #sebelum Setdefault
# print(Nilai)
# print("")

# #menggunakan setdefault
# print("Nilai : ", Nilai.setdefault("Kimia", 70))
# print("")

# #setelah menggunakan setdefault
# print(Nilai)

# Musik = {
# "The Chainsmoker" : ["All we Know", "TheParis"],
# "Alan Walker" : ["Alone", "Lily"],
# "Neffex" : ["Best of Me", "Memories"]
# }
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j:
#         print(song)
# print("")

# mahasiswa = {
# 101 : {"Nama" : "Aldy", "Umur" : 19 },
# 102 : {"Nama" : "Reja", "Umur" : 18}

# }


# for key, value in mahasiswa.items():
#     print("ID Mahasiswa : ", key)

# for key_a, value_a in value.items():
#     print (key_a, " : ", value_a)
# print("")




