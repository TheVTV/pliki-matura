with open('liczby.txt') as file:
    tab=[]
    for i in file:
        tab.append(i.split())


from collections import Counter

czestosc=[]

for liczby in tab:
    for litery in liczby[0]:
        czestosc.append(litery)
    for litery in liczby[1]:
        czestosc.append(litery)



x=Counter(czestosc)
suma=sum(x.values())
print(suma)
print(x)
essa=0
for klucz,wartosc in sorted(x.items()):
    print(klucz,':',round((wartosc/suma)*100,2),'%')
