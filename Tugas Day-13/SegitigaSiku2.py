import math


class SegitigaSiku2:
    def __init__(self):
        print("="*10, "Segitiga Siku-siku", 10*"=")
        self.a = int(input("Masukkan Alas Segitiga Siku-siku: "))
        self.t = int(input("Masukkan Tinggi Segitiga Siku-siku: "))
        self.m = math.sqrt(math.pow(self.t, 2) + math.pow(self.a, 2))

    def keliling(self):

        print("Keliling Segitiga Siku-siku:", "%.2f" %
              (self.a * self.t * self.m))

    def luas(self):
        print("Luas Segitiga Siku-siku:", 0.5 * self.a * self.t, "\n")
