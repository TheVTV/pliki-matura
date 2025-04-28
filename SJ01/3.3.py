with open('kebab.txt') as file:
    tab=[]
    for i in file:
        tab.append(int(i))
print(tab)


def zwijanie(x):
    czynniki = []
    i = 2
    while i*i<=x:
        while x % i == 0:
            czynniki.append(i)
            x //= i
        i += 1
    if x > 1:
        czynniki.append(x)
    return czynniki

def kebabowo(x):
    liczba=x
    zwinieta=sum(zwijanie(x))
    dlugosc=1
    liczba=x
    poprzednia=0
    while poprzednia!=zwinieta:
        poprzednia=x
        dlugosc+=1
        zwinieta=sum(zwijanie(x))
        liczba+=zwinieta
        x=zwinieta
    return liczba


zwiniete=[]

for liczba in tab:
    zwiniete.append(kebabowo(liczba))
print(zwiniete)

def kebabowa(x):
    zwinieta=sum(zwijanie(x))
    dlugosc=1
    liczba=x
    poprzednia=0
    parzyste=0
    nieparzyste=0
    while poprzednia!=zwinieta:
        poprzednia=x
        if poprzednia % 2 == 0:
            parzyste += 1
        else:
            nieparzyste += 1
        dlugosc+=1
        zwinieta=sum(zwijanie(x))
        liczba+=zwinieta
        x=zwinieta
    if poprzednia % 2 == 0:
        parzyste += 1
    else:
        nieparzyste += 1

    if parzyste==nieparzyste:
        return True
    else:
        return False
print(kebabowa(20))

licznik=0

for liczba in zwiniete:
    if kebabowa(liczba):
        licznik+=1

print(licznik)

def dzielniki(x):
    czynniki=[]
    for i in range(1,x):
        if x%i==0:
            czynniki.append(i)
    return czynniki

print(dzielniki(12))
licz=0

for liczba in zwiniete:
    if sum(dzielniki(liczba))==liczba:
        licz+=1

print(licz)