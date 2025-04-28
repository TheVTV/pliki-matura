def czynniki(n):
    czynniki_list = []
    i = 2
    while n>1:
        while n%i==0:
            czynniki_list.append(i)
            n//=i
        i+=1
    return sum(czynniki_list)


def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True


with open("kebab.txt","r") as file:
    dane = [int(x.strip()) for x in file]

wyniki = [[[]for _ in range(2)] for _ in range(len(dane))]
maks = 0
for i in range(0, len(dane)):
    liczba = dane[i]
    zwijanie = 3
    n = czynniki(liczba)
    suma = n+liczba
    while not prime(n):
        zwijanie += 1
        if zwijanie > maks:
            maks = zwijanie
        n = czynniki(n)
        suma += n
    wyniki[i][0] = liczba
    wyniki[i][1] = zwijanie
print(maks)
for i in range(0, len(dane)):
    if wyniki[i][1]==maks:
        print(wyniki[i][0])
