with open('liczby.txt') as a:
    a=a.readlines()
wyn={}
suma=0
sys="0123456789ABCDEF"
for linijka in a:
    linijka=linijka.split()
    for x in range(2):
        for litera in sys:
            if litera not in wyn and litera in linijka[x]:
                wyn[litera]=1
            if litera in wyn and litera in linijka[x]:
                wyn[litera]+=1
for liczba in sys:
    suma+=wyn[liczba]
for liczba in sys:
    wyn[liczba]=str(round(wyn[liczba]*100/suma,2))+'%'
print(wyn)