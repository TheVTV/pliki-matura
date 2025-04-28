czestotliwosci = {char: 0 for char in "0123456789ABCDEF"}

wszystkie_znaki = 0

with open("liczby.txt", "r") as plik:
    for linia in plik:
        a, b = linia.strip().split('\t')
        for liczba in [a, b]:
            for znak in liczba:
                if znak in czestotliwosci:
                    czestotliwosci[znak] += 1
                    wszystkie_znaki += 1

for znak in "0123456789ABCDEF":
    if wszystkie_znaki > 0:
        czestotliwosc = czestotliwosci[znak] / wszystkie_znaki * 100
        print(f"{znak}: {czestotliwosc:.2f}%")
    else:
        print(f"{znak}: 0.00%")
