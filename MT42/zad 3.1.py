pierwsze=[]
for x in range(2, 10000):
    pierwsza = True
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            pierwsza = False
            break
    if pierwsza:
        pierwsze.append(x)

with open('kebab_przyklad.txt') as a:
    a=a.readlines()
suma=0
petl=0
pm=0
for liczba in a:
    liczba=int(60)
    suma=liczba
    while liczba not in pierwsze:
        petl+=1
        for tab in range(liczba//2):
            if liczba%pierwsze[tab]==0:
                liczba=liczba//pierwsze[tab]
                suma+=pierwsze[tab]
                petl+=1
                break
    if pm<petl:
        pm=petl
    ws=suma+liczba
    suma=0
    petl=0
print(pm)
















