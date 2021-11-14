print("-" * 10, "Cetak angka 1 - 10", "-" * 10)
angka = 10
for i in range(angka):
    i += 1
    print("Angka", i)

print("-" * 10, "Cetak bilangan genap dari angka 1 - 10", "-" * 10)
angka = 10
for i in range(angka):
    i += 1
    if(i % 2 == 0):
        print("Bilangan Genap", i)
