def topish(s):
    harflar = {}
    takrorlanuvchilar = []

    for harf in s:
        if harf in harflar:
            harflar[harf] += 1
        else:
            harflar[harf] = 1

    for harf, son in harflar.items():
        if son > 1:
            takrorlanuvchilar.append(harf)

    return takrorlanuvchilar

s = input("Istalgan matn kiriting: ")
print(topish(s))
