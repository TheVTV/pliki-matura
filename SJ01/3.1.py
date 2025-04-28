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

print(zwijanie(60))


def kebabowa(x):
    pierwsza=x
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
    return [pierwsza,dlugosc]

print(kebabowa(60))

zwiniete=[]

for liczba in tab:
    zwiniete.append(kebabowa(liczba))

print(zwiniete)
max=0
for liczba in zwiniete:
    if liczba[1]>max:
        max=liczba[1]
print(max)

for liczba in zwiniete:
    if liczba[1]==max:
        print(liczba[0])

