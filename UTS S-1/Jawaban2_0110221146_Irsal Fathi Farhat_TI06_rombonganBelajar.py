# Diketahui:
# •	Pegawai 1 Ahmad muslim memiliki gaji pokok  Rp.4.000.00 dan  memiliki dua orang anak.
# •	Pegawai 2 Alex beragama Kristen Protestan memiliki gaji pokok  Rp. 6.000.000 dan memiliki 5 orang anak.
# Soal:
# Buat aplikasi sederhana dengan pemrograman python untuk mencetak :
# Nama pegawai, agama, gaji pokok, tunjangan jabatan, tunjangan keluarga, gaji kotor, zakat profesi, gaji bersih (take home pay).
# Kalkulasi:
# •	Tunjangan jabatan 20% dari gaji pokok
# •	Tunjangan keluarga (gunakan if multi kondisi):
# 	Jika jumlah anak maksimal 2 anak, tunjangan keluarga 10% dari gaji pokok
# 	Jika jumlah anak lebih dari 2 orang, tunjangan keluarga 20% dari gaji pokok
# 	Jika belum mempunyai anak, belum dapat tunjangan keluarga
# •	Gaji Kotor = Gaji Pokok + Tunjangan Jabatan + Tunjangan Keluarga
# •	Zakat profesi hanya untuk pegawai muslim dan memiliki gaji kotornya lebih dari Rp. 6.000.000. Zakat profesi sebesar 2,5% dari total gaji kotor. (Gunakan Tuple & List).
# (0, 0.025)[jika agama == “Islam” and gaji_kotor >= 6000000] * gaji_kotor
# •	Gaji bersih = Gaji Kotor – Zakat Profesi
print("-" * 10, "Belanja Online", "-" * 10, "\n")

pembeli = str(input("Masukkan nama anda: "))

print("""Produk yang kami sediakan:
1. Kipas Angin\t: Rp. 1000000
2. TV\t\t: Rp. 2000000
3. Mesin Cuci\t: Rp. 3000000
4. AC\t\t: Rp. 4000000
5. Kulkas\t: Rp. 5000000""")

produk = int(input("Pilih no. produk yang ingin dibeli: "))

while True:
    if(produk == 1):
        namaProduk = "Kipas Angin"
        harga = 1000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(jumlahBarang >= 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 2):
        namaProduk = "TV"
        harga = 2000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(jumlahBarang >= 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 3):
        namaProduk = "Mesin Cuci"
        harga = 3000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(jumlahBarang >= 1):
            diskon = totalPembelian * 0.05
        else:
            diskon = 0
        break
    elif(produk == 4):
        namaProduk = "AC"
        harga = 4000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(jumlahBarang >= 5):
            diskon = totalPembelian * 0.10
        else:
            diskon = 0
        break
    elif(produk == 5):
        namaProduk = "Kulkas"
        harga = 5000000
        jumlahBarang = int(input("Masukkan jumlah barang yang ingin dibeli: "))
        totalPembelian = harga * jumlahBarang
        if(jumlahBarang >= 5):
            diskon = totalPembelian * 0.20
        else:
            diskon = 0
        break
    else:
        print("Masukkan angka yang sesuai")
        produk = int(input("Pilih no. produk yang ingin dibeli: "))
        continue

hargaKotor = totalPembelian
ppn = (hargaKotor - diskon) * 0.10
hargaBersih = (hargaKotor - diskon) + ppn

print("""Nama Anda\t: %s
Produk Pilihan\t: %s
Harga Produk\t: Rp. %s
Jumlah Beli\t: %ipcs
Harga Kotor\t: Rp. %i
Diskon\t\t: Rp. %i
PPN 10%%\t\t: Rp. %i
Harga Bersih\t: Rp. %i
""" % (pembeli, namaProduk, harga, jumlahBarang, hargaKotor, diskon, ppn, hargaBersih))
print("-" * 10, "Terimakasih sudah berbelanja disini", "-" * 10)
