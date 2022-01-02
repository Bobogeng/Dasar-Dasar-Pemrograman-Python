class PersegiPanjang:
    def __init__(self):
        print("="*10, "Persegi Panjang", 10*"=")
        self.p = int(input("Masukkan Panjang Persegi Panjang: "))
        self.l = int(input("Masukkan Lebar Persegi Panjang: "))

    def keliling(self):
        print("Keliling Persegi Panjang:", 2 * (self.p + self.l))

    def luas(self):
        print("Luas Persegi Panjang:", self.p * self.l, "\n")
