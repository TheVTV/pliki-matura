with open('liczby.txt') as a:
    a=a.readlines()
min=float('inf')
max=0
smin=0
smax=0
for linijka in a:
    linijka=linijka.split()
    for sys in range(2,17):
        try:
            if str(int(linijka[0], sys))==str(int(linijka[1],sys))[::-1]:
                liczba1=int(linijka[0],sys)
                liczba2=int(linijka[1],sys)
                if liczba1>max:
                    max=liczba1
                    smax=linijka[0]
                if liczba2>max:
                    max=liczba2
                    smax=linijka[1]
                if liczba1<min:
                    min=liczba1
                    smin=linijka[0]
                if liczba2<min:
                    min=liczba2
                    smin=linijka[1]
        except ValueError:
            continue
print(smin,smax)