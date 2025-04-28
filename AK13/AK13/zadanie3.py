
def rozkladNaCzynnikiPierwsze(liczba):
    i = 2
    suma = 0
    while liczba > 1:
        if liczba % i == 0:
            liczba = liczba / i

            suma += i
        else:
            i += 1
    return suma

def procesZawijania(liczba):
    dlugosc = 1
    while True:
        if rozkladNaCzynnikiPierwsze(liczba) != liczba:
            dlugosc += 1
            liczba = rozkladNaCzynnikiPierwsze(liczba)
        else:
            break
    return dlugosc + 1

def liczbaKebabowa(liczba):
    liczbaKebabowa1 = liczba
    while True:
        if rozkladNaCzynnikiPierwsze(liczba) != liczba:
            liczba = rozkladNaCzynnikiPierwsze(liczba)
            liczbaKebabowa1 += liczba
        else:
            break
    return liczbaKebabowa1 + liczba

def czyPalindrom(string):
    return string == string[::-1]

def czyliczbaPierwsza(liczba):
    if liczba < 2:
        return False

    for i in range(2, liczba):
        if liczba % i == 0:
            return False
    return True

def procesZawijaniaCzyTyleSamoParzystych(liczba):
    dlugosc = 1
    parzyste = 0
    nieparzyste = 0
    tablica = [liczba]


    while True:
        if rozkladNaCzynnikiPierwsze(liczba) != liczba:
            dlugosc += 1
            liczba = rozkladNaCzynnikiPierwsze(liczba)
            tablica.append(liczba)
        else:
            break
    tablica.append(liczba)

    for element in tablica:
        if element % 2 == 0:
            parzyste +=1
        else:
            nieparzyste += 1
    return nieparzyste == parzyste

def czySumaDzielnikowWlasciwychRownaLiczbie(liczba):
    suma = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            suma += i
    return suma == liczba


def zad3_1():

    plik = open("kebab.txt")
    najdluzszyProcesZawijania = 0
    tablica = []
    for line in plik:
        liczba1 = int(line.strip())

        procesZawijania1 = procesZawijania(liczba1)
        if procesZawijania1 > najdluzszyProcesZawijania:
            najdluzszyProcesZawijania = procesZawijania1
            tablica = [liczba1]
        elif procesZawijania1 == najdluzszyProcesZawijania:
            tablica.append(liczba1)

    wynik = f"""{procesZawijania(tablica[0])}
{tablica[0]}
{tablica[1]}"""

    plik.close()
    return wynik

def zad3_2():

    plik = open("kebab.txt")
    ilePalindromow = 0
    ileLiczbPierwszych = 0
    for line in plik:
        liczba1 = int(line.strip())
        liczbaKebabowa1 = liczbaKebabowa(liczba1)

        if czyPalindrom(str(liczbaKebabowa1)):
            ilePalindromow += 1
        if czyliczbaPierwsza(liczbaKebabowa1):
            ileLiczbPierwszych += 1

    wynik = f"{ilePalindromow} {ileLiczbPierwszych}"
    plik.close()
    return wynik

def zad3_3():
    ileTakich = 0
    plik = open("kebab.txt")
    for line in plik:
        liczba1 = int(line.strip())
        if procesZawijaniaCzyTyleSamoParzystych(liczba1):
            ileTakich += 1

    plik.close()
    return ileTakich

def zad3_4():
    ileTakich = 0
    plik = open("kebab.txt")
    for line in plik:
        liczba1 = int(line.strip())
        liczbaKebabowa1 = liczbaKebabowa(liczba1)

        if czySumaDzielnikowWlasciwychRownaLiczbie(liczbaKebabowa1):
            ileTakich += 1
    plik.close()
    return ileTakich

zapis = open("wyniki3.txt", "w")

wynik1 = zad3_1()
wynik2 = zad3_2()
wynik3 = zad3_3()
wynik4 = zad3_4()

zapis.write("3.1)\n")
zapis.write(f"{wynik1}\n")
zapis.write("\n")

zapis.write("3.2)\n")
zapis.write(f"{wynik2}\n")
zapis.write("\n")

zapis.write("3.3)\n")
zapis.write(f"{wynik3}\n")
zapis.write("\n")

zapis.write("3.4)\n")
zapis.write(f"{wynik4}\n")
zapis.write("\n")

zapis.close()