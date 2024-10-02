# nama = ["shandy",106,True,["yuyun",145],3.96,[123,"ALVITO",False,3.66],"rehan"]
# matkul =["APD","APL","WEB","jarkom","BASDAT","STRUKDAT","PTI","KALKULUS","PROBAS"]

# print(matkul[-3])

# makanan = ["Bakso","Sate","Soto","nasi goreng","mie ayam","ayam bakar","cumi goreng"]
# print(makanan)
# print("Sebelum:")

# makanan.append("Nasi Goreng")
# print(makanan)
# print("Sesudah")

# makanan.insert(0,"Nasi goreng")
# print(makanan)

# makanan[0] ="Indomie"
# makanan[1] ="telor dadar"
# print(makanan)

# del makanan[:5]
# print(makanan)

# data = makanan.pop(5)
# print(makanan)
# print(data)

# for i in makanan:
#     print(i, end=",")

makanan = ["ayam bakar","telur rebus",["indomie","Telur dadar"],["mie ayam","ayam bakar","cumi goreng"]]

for i in makanan:
    if isinstance(i,list):
        for j in i:
            print(j,end=",")
    else:
        print(i,end=",")

# minuman= ["susu","Jus mangga","Jus sirsak","es teler","es teh","es buah"]
# print("Sebelum")
# print(minuman)

# del minuman[2]
# print("Sesudah")
# print(minuman)

# minuman[4] ="air putih"
# print(minuman)

# minuman.insert(0,"jus tomat")
# print(minuman)