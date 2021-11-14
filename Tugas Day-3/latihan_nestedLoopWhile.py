string = ""
bar = 1
# Looping Baris
while bar <= 5:
    kol = bar
    # Looping Kolom
    while kol > 0:
        string += "* "
        kol = kol - 1
    string += "\n"
    bar = bar + 1
print(string)
