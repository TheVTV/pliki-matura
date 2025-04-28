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
ileFalafel = 0
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
    tab = []
    sumaDzielnikow = 0
    for j in range(1, liczbaKebabowa):
        if liczbaKebabowa % j == 0:
            tab.append(j)
    for j in tab:
        sumaDzielnikow = sumaDzielnikow + j
    if sumaDzielnikow == liczbaKebabowa:
        ileFalafel +=1
print(ileFalafel)