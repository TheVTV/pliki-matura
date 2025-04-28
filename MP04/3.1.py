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
maksymalna = 0
for i in dane:
    dlugoscZwijania = 1
    liczba = int(i)
    wczesniejszaLiczba = 0
    while liczba != wczesniejszaLiczba:
        nowaLiczba = 0
        for j in rozkladNaCzynniki(liczba):
            nowaLiczba = nowaLiczba + j
        wczesniejszaLiczba = liczba
        liczba = nowaLiczba
        dlugoscZwijania+=1
    if dlugoscZwijania>maksymalna:
        maksymalna = dlugoscZwijania
print(maksymalna)
for i in dane:
    dlugoscZwijania = 1
    liczba = int(i)
    wczesniejszaLiczba = 0
    while liczba != wczesniejszaLiczba:
        nowaLiczba = 0
        for j in rozkladNaCzynniki(liczba):
            nowaLiczba = nowaLiczba + j
        wczesniejszaLiczba = liczba
        liczba = nowaLiczba
        dlugoscZwijania+=1
    if dlugoscZwijania==maksymalna:
        print(int(i))