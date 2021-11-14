print("-" * 10, "Segitiga Siku-siku Kanan", "-" * 10)
a = 5
for i in range(0, a):
    for j in range(0, i + 1):
        print("* ", end="")
    print("")

print("-" * 10, "Segitiga Siku-siku Kiri", "-" * 10)
a = 5
for i in range(0, a):
    print("* ", end="")
    for j in range(0, a - 1):
        print("* ", end="")
    a -= 1
    print("")

print("-" * 10, "Segitiga Sama Kaki", "-" * 10)
a = 5
s = a
for i in range(0, a):
    s -= 1
    for j in range(0, s):
        print(" ", end="")
    for k in range(0, i + 1):
        print("* ", end="")
    print("")

print("-" * 10, "Segitiga Sama Kaki", "-" * 10)
a = 5
s = a - a
for i in range(0, a):
    for j in range(0, s):
        print(" ", end="")
    s += 1
    for k in range(0, a):
        print("* ", end="")
    a -= 1
    print("")

print("-" * 10, "Segitiga Pascal", "-" * 10)
a = 5
s = a
for i in range(0, a):
    for j in range(0, s):
        print(" ", end="")
    s -= 1
    for k in range(0, i + 1):
        print("* ", end="")
    print("")
print((a + 1) * "* ")
for i in range(0, a):
    s += 1
    for j in range(0, s):
        print(" ", end="")
    for k in range(0, a):
        print("* ", end="")
    a -= 1
    print("")
