with open("liczby.txt", "r") as file:
    dane = [line.strip().split("\t") for line in file]


def systemy(n):
    lista = "123456789ABCDEF"
    maks = "0"
    for i in n:
        if i > maks:
            maks = i
    for i in range(0, 16):
        if maks == lista[i]:
            return i + 2

liczby = []
for x, y in dane:
    liczby.append(int(x, systemy(x)))
    liczby.append(int(y, systemy(y)))
print(max(liczby))