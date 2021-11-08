print("-" * 10, "Belanja Online", "-" * 10, "\n")

pembeli = str(input("Masukkan nama anda: "))

print("""Produk yang kami sediakan:
1. Kipas Angin\t= Rp. 1000000
2. TV\t\t= Rp. 2000000
3. Mesin Cuci\t= Rp. 3000000
4. AC\t\t= Rp. 4000000
5. Kulkas\t= Rp. 5000000""")

produk = int(input("Pilih no. produk yang ingin dibeli: "))

while True:
    if(produk == 1):
        namaProduk = "Kipas Angin"
        harga = 1000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(totalPembelian > 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 2):
        namaProduk = "TV"
        harga = 2000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(totalPembelian > 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 3):
        namaProduk = "Mesin Cuci"
        harga = 3000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(totalPembelian > 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 4):
        namaProduk = "AC"
        harga = 4000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(totalPembelian >= 3):
            diskon = totalPembelian * 0.10
        else:
            diskon = 0
        break
    elif(produk == 5):
        namaProduk = "Kulkas"
        harga = 5000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(totalPembelian >= 5):
            diskon = totalPembelian * 0.20
        else:
            diskon = 0
        break
    else:
        print("Masukkan angka yang sesuai")
        produk = int(input("Pilih no. produk yang ingin dibeli: "))
        continue

hargaKotor = totalPembelian + diskon
ppn = totalPembelian * 0.10
hargaBersih = totalPembelian + ppn

print("""Nama Anda\t: %s"
Produk Pilihan\t: %s
Harga Produk\t: Rp. %s
Jumlah Beli\t: %ipcs
Harga Kotor\t: Rp. %i
Diskon\t\t: Rp. %i
PPN 10%%\t\t: Rp. %i
""" % (pembeli, namaProduk, harga, jumlahBarang, hargaKotor, diskon, ppn))
print("-" * 10, "Terimakasih sudah berbelanja di Belanja Online", "-" * 10)
