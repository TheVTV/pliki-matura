wejscie = open("kebab.txt", "r")
wyjscie = open("wyniki3.txt", "w")

dane = [int(line.strip()) for line in wejscie.readlines()]

def czynniki_pierwsze(n):
    czynniki = []

    if n % 2 == 0:
        while n % 2 == 0:
            czynniki.append(2)
            n //= 2

    d = 3

    while (d * d) <= n:
        if n % d == 0:
            while n % d == 0:
                czynniki.append(d)
                n //= d
        d += 2

    if n > 1:
        czynniki.append(n)

    return czynniki

def zwijanie(n):
    prev = None
    current = n

    zwijanie = []

    while True:
        zwijanie.append(current)
        if current == prev:
            return zwijanie
        prev = current
        current = sum(czynniki_pierwsze(prev))

# print(zwijanie(60))

def zadanie31(dane, wyjscie):
    print("3.1.", file = wyjscie)
    maxlen = 0
    maxi_dlugosci = []

    for liczba in dane:
        maxlen = max(maxlen, len(zwijanie(liczba)))

    for liczba in dane:
        if len(zwijanie(liczba)) == maxlen:
            maxi_dlugosci.append(liczba)

    print(maxlen, file = wyjscie)

    for maxi in maxi_dlugosci:
        print(maxi, file = wyjscie)

def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def palindrom(n):
    s = str(n)
    return s == s[::-1]

def liczba_kebabowa(n):
    proces = zwijanie(n)
    return sum(proces)

def zadanie32(dane, wyjscie):
    print("3.2.", file = wyjscie)

    kebab_palindrom = 0
    kebab_pierwsza  = 0

    for liczba in dane:
        liczba_k = liczba_kebabowa(liczba)
        if palindrom(liczba_k):
            kebab_palindrom += 1
        if prime(liczba_k):
            kebab_pierwsza += 1

    print(kebab_palindrom, kebab_pierwsza, file = wyjscie)

def mm_kebab(n):
    proces = zwijanie(n)
    np, p = 0, 0
    for liczba in proces:
        if liczba % 2 == 0:
            p += 1
        else:
            np += 1
    return np == p

def zadanie33(dane, wyjscie):
    print("3.3.", file = wyjscie)

    mieciane_mieciane = 0

    for liczba in dane:
        if mm_kebab(liczba):
            mieciane_mieciane += 1

    print(mieciane_mieciane, file = wyjscie)

def dzielniki_wlasciwe(n):
    dzielniki_w = []

    for i in range(1, n):
        if n % i == 0:
            dzielniki_w.append(i)

    return dzielniki_w

# nie wiem kto sprawdza te zadania ale chcialam powiedziec ze kocham falafel <3
def falafel(liczba_k):
    suma_dzielnikow_wlasciwych = sum(dzielniki_wlasciwe(liczba_k))

    if suma_dzielnikow_wlasciwych == liczba_k:
        return True
    return False

def zadanie34(dane, wyjscie):
    print("3.4.", file = wyjscie)

    falafelki = 0

    for liczba in dane:
        liczba_kebs = liczba_kebabowa(liczba)
        if falafel(liczba_kebs):
            falafelki += 1

    print(falafelki, file =  wyjscie)


zadanie31(dane, wyjscie)
zadanie32(dane, wyjscie)
zadanie33(dane, wyjscie)
zadanie34(dane, wyjscie)

wejscie.close()
wyjscie.close()