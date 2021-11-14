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
anak1 = 2
anak2 = 5
agama1 = "Islam"
agama2 = "Kristen"

pegawai = ["Ahmad", "Alex"]
gajiPokok = [4000000, 6000000]
tunjanganJabatan = [number * 0.20 for number in gajiPokok]
tunjanganKeluarga1 = gajiPokok

if (anak1 > 0 and anak1 <= 2):
    tunjanganKeluarga1 = [number * 0.10 for number in gajiPokok]
elif (anak1 > 2):
    tunjanganKeluarga1 = [number * 0.20 for number in gajiPokok]
else:
    tunjanganKeluarga1 = [number * 0 for number in gajiPokok]

if (anak2 > 0 and anak2 <= 2):
    tunjanganKeluarga2 = [number * 0.10 for number in gajiPokok]
elif (anak2 > 2):
    tunjanganKeluarga2 = [number * 0.20 for number in gajiPokok]
else:
    tunjanganKeluarga2 = [number * 0 for number in gajiPokok]


gajiKotor1 = [gajiPokok[0], tunjanganJabatan[0], tunjanganKeluarga1[0]]
gajiKotor2 = [gajiPokok[1], tunjanganJabatan[1], tunjanganKeluarga2[1]]
gajiKotorSum1 = sum(map(float, gajiKotor1))
gajiKotorSum2 = sum(map(float, gajiKotor2))

zakatProfesi1 = (0, gajiKotorSum1 *
                 0.025)[gajiKotorSum1 >= 6000000.0 and agama1 == "Islam"]
zakatProfesi2 = (0, gajiKotorSum2 *
                 0.025)[gajiKotorSum2 >= 6000000.0 and agama2 == "Islam"]

gajiBersih1 = gajiKotorSum1 - zakatProfesi1
gajiBersih2 = gajiKotorSum2 - zakatProfesi2

print("SLIP GAJI PT. XYZ")
print("-" * 10)
print("Nama Pegawai \t\t:", pegawai[0], "\n"
      "Agama \t\t\t:", agama1, "\n"
      "Jumlah Anak \t\t:", anak1, "\n"
      "Gaji Pokok \t\t: Rp.", gajiPokok[0], "\n"
      "Tunjangan Jabatan \t: Rp.", tunjanganJabatan[0], "\n"
      "Tunjangan Keluarga \t: Rp.", tunjanganKeluarga1[0], "\n"
      "Gaji Kotor \t\t: Rp.", gajiKotorSum1, "\n"
      "Zakat Profesi \t\t: Rp.", zakatProfesi1, "\n"
      "Take Home Pay \t\t: Rp.", gajiBersih1
      )
print("SLIP GAJI PT. XYZ")
print("-" * 10)
print("Nama Pegawai \t\t:", pegawai[1], "\n"
      "Agama \t\t\t:", agama2, "\n"
      "Jumlah Anak \t\t:", anak2, "\n"
      "Gaji Pokok \t\t: Rp.", gajiPokok[1], "\n"
      "Tunjangan Jabatan \t: Rp.", tunjanganJabatan[1], "\n"
      "Tunjangan Keluarga \t: Rp.", tunjanganKeluarga2[1], "\n"
      "Gaji Kotor \t\t: Rp.", gajiKotorSum2, "\n"
      "Zakat Profesi \t\t: Rp.", zakatProfesi2, "\n"
      "Take Home Pay \t\t: Rp.", gajiBersih2
      )
