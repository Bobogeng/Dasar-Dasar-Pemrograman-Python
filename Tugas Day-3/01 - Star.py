w = 3
p = w
a = w
s = a * 3
for i in range(0, a):
    s -= 1
    for j in range(0, s):
        print(" ", end="")
    for k in range(0, i + 1):
        print("* ", end="")
    print("")

a = a * 3
s = a - a
for i in range(0, w):
    for j in range(0, s):
        print(" ", end="")
    s += 2
    for k in range(0, a):
        print("* ", end="")
    a -= 2
    print("")

a = a * 2
s = w + 1
for i in range(0, w):
    s -= 1
    for z in range(0, s):
        print(" ", end="")
    for j in range(0, w):
        print("* ", end="")
    for l in range(i):
        print(" " * 6, end="")
    for k in range(0, w):
        print("* ", end="")
    w -= 1
    print("")
