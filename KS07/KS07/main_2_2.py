import collections
from collections import Counter
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

wyniki = []
for x, y in dane:
    wyniki.append(max(systemy(x), systemy(y)))
print(wyniki)
for x, y in sorted(collections.Counter(wyniki).items()):
    print(x,y)