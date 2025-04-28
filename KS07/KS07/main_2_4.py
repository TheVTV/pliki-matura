import collections

with open("liczby.txt", "r") as file:
    dane = [line.strip().split("\t") for line in file]

znaki = []
licznik = 0
for x,y in dane:
    for i in x:
        znaki.append(i)
        licznik += 1
    for i in y:
        znaki.append(i)
        licznik += 1

from collections import Counter
for x, y in sorted(collections.Counter(znaki).items()):
    print(x, round(y/licznik*100, 2),end="")
    print("%")
print(licznik)