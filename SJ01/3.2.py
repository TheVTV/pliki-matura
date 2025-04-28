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


def kebabowa(x):
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
    zwiniete.append(kebabowa(liczba))
print(zwiniete)

def pierwsza(x):
    if x==0 or x==1:
        return False
    for i in range(2,int(x**1/2)+1):
        if x%i==0:
            return False
    return True

palindromy=0
pierwsze=0
for liczba in zwiniete:
    if str(liczba)==str(liczba)[::-1]:
        palindromy+=1
    if pierwsza(liczba):
        pierwsze+=1

print(palindromy,pierwsze)