def ktory_system(n,L):
    liczba=15
    najwieksza='-'
    for i in range(L):
        if n[i]>najwieksza:
            najwieksza=n[i]
    if najwieksza=='1':
        return 2
    elif najwieksza=='2':
        return 3
    elif najwieksza=='3':
        return 4
    elif najwieksza=='4':
        return 5
    elif najwieksza=='5':
        return 6
    elif najwieksza=='6':
        return 7
    elif najwieksza=='7':
        return 8
    elif najwieksza=='8':
        return 9
    elif najwieksza=='9':
        return 10
    elif najwieksza=='A':
        return 11
    elif najwieksza=='B':
        return 12
    elif najwieksza=='C':
        return 13
    elif najwieksza=='D':
        return 14
    elif najwieksza=='E':
        return 15
    elif najwieksza=='F':
        return 16

print(ktory_system('1BCD9',5))




with open('liczby.txt') as file:
    tab=[]
    for i in file:
        tab.append(i.split())
print(tab)
print(int('36470',13),int('AA30',13))

from collections import Counter

tabela=[]

for liczby in tab:
    for systemy in range(17,1,-1):
        if int(liczby[0],systemy)==int(str(int(liczby[1],systemy))[::-1]):
            tabela.append(systemy)
            break

print(tabela)



print(Counter(tabela))

for klucz,wartosc in sorted(Counter(tabela).items()):
    print(klucz,':',wartosc)

