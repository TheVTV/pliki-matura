with open (r'C:\Users\student7\PyCharmMiscProject\kebab.txt') as file:
    # C:\Users\student7\PyCharmMiscProject\kebab.txt
    # C:\Users\student7\PyCharmMiscProject\kebab_przyklad.txt
    dane=[]
    for i in file:
        dane.append(i.strip())
def rozkladNaCzynniki(liczba):
    tab = []
    i = 2
    while liczba != 1:
        if liczba % i == 0:
            liczba = liczba // i
            tab.append(i)
        else:
            i += 1
    return tab
def czyPierwsza(liczba):
    for i in range (2,liczba):
        if liczba % i == 0:
            return False
    return True
ilePalindromow = 0
ilePierwszych = 0
for i in dane:
    liczba = int(i)
    liczbaKebabowa = liczba
    wczesniejszaLiczba = 0
    while liczba != wczesniejszaLiczba:
        nowaLiczba = 0
        for j in rozkladNaCzynniki(liczba):
            nowaLiczba = nowaLiczba + j
        wczesniejszaLiczba = liczba
        liczba = nowaLiczba
        liczbaKebabowa = liczbaKebabowa + liczba
    if str(liczbaKebabowa) == str(liczbaKebabowa)[::-1]:
        ilePalindromow += 1
    if czyPierwsza(liczbaKebabowa):
        ilePierwszych += 1
print(f"{ilePalindromow}  {ilePierwszych}")