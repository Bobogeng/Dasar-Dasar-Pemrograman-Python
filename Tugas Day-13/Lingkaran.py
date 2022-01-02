import math


class Lingkaran:
    def __init__(self):
        print("="*10, "Lingkaran", 10*"=")
        self.r = int(input("Masukkan Jari-jari Lingkaran: "))

    def keliling(self):
        print("Keliling Lingkaran:", "%.1f" % (2 * math.pi * self.r))

    def luas(self):
        print("Luas Lingkaran:", "%.1f" % (math.pi * pow(self.r, 2)), "\n")
