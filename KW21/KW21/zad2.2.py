plik = open(".\liczby.txt", "r")
linie = plik.readlines()
linie_gotowe = []

for i in linie:
    p = i.partition("\t")
    linie_gotowe.append([p[0], p[2][:-1]])
print(linie_gotowe)


def jaki_system(n):
    m = 0
    for i in n:
        if i == "F" and m < 16:
            m = 16
        elif i == "E" and m < 15:
            m = 15
        elif i == "D" and m < 14:
            m = 14
        elif i == "C" and m < 13:
            m = 13
        elif i == "B" and m < 12:
            m = 12
        elif i == "A" and m < 11:
            m = 11
        elif i == "9" and m < 10:
            m = 10
        elif i == "8" and m < 9:
            m = 9
        elif i == "7" and m < 8:
            m = 8
        elif i == "6" and m < 7:
            m = 7
        elif i == "5" and m < 6:
            m = 6
        elif i == "4" and m < 5:
            m = 5
        elif i == "3" and m < 4:
            m = 4
        elif i == "2" and m < 3:
            m = 3
        elif (i == "1" or i == "0") and m < 2:
            m = 2
    return m

print(jaki_system("1"))
print(jaki_system("AF"))

statystyki = {}

for i in linie_gotowe:
    wynik = jaki_system(i[0])
    if statystyki.get(wynik) is None:
        statystyki[wynik] = 1
    else:
        statystyki[wynik] += 1

print(statystyki)

with open("wyniki2.txt", "w") as f:
    f.write("2.2\n")
    for i in range(2, 17):
        f.write(f"{i}: {statystyki.get(i)}\n")

plik.close()