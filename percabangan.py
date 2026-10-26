# # input
# nilai =int(input("Masukkan nilai: "))
# # proses
# if nilai >= 80 and nilai<=100:
#     print("Anda mendapatkan nilai A")
# elif nilai >=70 and nilai <=80:
#     print("Anda mendapatkan nilai B")
# elif nilai >=50 and nilai <=70:
#     print("Anda mendapatkan nilai c")
# elif nilai >=30 and nilai <=50:
#     print("Anda mendapatkan nilai D")
# elif nilai >=0 and nilai <=20:
#     print("Anda mendapatkan nilai E")
# else:
#     print("Data tidak valid")
# print("==========Latihan======")
#input
barang = input("masukkan nama barang:")
harga = int(input("masukkan harga: "))
#proses
if barang =="kulkas":
    print(barang)
    print(harga - (0.10 * harga))
elif barang =="tv":
    print(barang)
    print(harga - (0.50 * harga))
else:
    print(barang)
    print(harga)