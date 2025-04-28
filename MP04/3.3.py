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
ileMiecian = 0
for i in dane:
    ileParzystych = 0
    ileNieparzystych = 0
    liczba = int(i)
    if liczba %2 == 0:
        ileParzystych += 1
    else:
        ileNieparzystych += 1
    wczesniejszaLiczba = 0
    while liczba != wczesniejszaLiczba:
        nowaLiczba = 0
        for j in rozkladNaCzynniki(liczba):
            nowaLiczba = nowaLiczba + j
        wczesniejszaLiczba = liczba
        liczba = nowaLiczba
        if liczba % 2 == 0:
            ileParzystych += 1
        else:
            ileNieparzystych += 1
    if ileParzystych == ileNieparzystych:
        ileMiecian += 1
print(ileMiecian)