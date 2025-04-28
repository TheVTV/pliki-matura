

#podane L, dlugosc
# oraz n, napis (string)

napis='1BCD9'
dlugosc=len(napis)

def ile_systemów(n,L):
    liczba=15
    najwieksza='-'
    for i in range(L):
        if n[i]>najwieksza:
            najwieksza=n[i]
    if najwieksza=='1':
        k=liczba-1+1
    elif najwieksza=='2':
        k=liczba-2+1
    elif najwieksza=='3':
        k=liczba-3+1
    elif najwieksza=='4':
        k=liczba-4+1
    elif najwieksza=='5':
        k= liczba-5+1
    elif najwieksza=='6':
        k=liczba-6+1
    elif najwieksza=='7':
        k=liczba-7+1
    elif najwieksza=='8':
        k=liczba-8+1
    elif najwieksza=='9':
        k=liczba-9+1
    elif najwieksza=='A':
        k=liczba-10+1
    elif najwieksza=='B':
        k=liczba-11+1
    elif najwieksza=='C':
        k=liczba-12+1
    elif najwieksza=='D':
        k=liczba-13+1
    elif najwieksza=='E':
        k=liczba-14+1
    elif najwieksza=='F':
        k=liczba-15+1
    return k

print(ile_systemów(napis,dlugosc))

