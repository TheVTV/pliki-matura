with open('liczby.txt') as a:
    a=a.readlines()
wyn={}
for linijka in a:
    linijka=linijka.split()
    for sys in range(2,17):
        try:
            if str(int(linijka[0], sys))==str(int(linijka[1],sys))[::-1]:
                if sys not in wyn:
                    wyn[sys]=1
                else:
                   wyn[sys]+=1
        except ValueError:
            continue
print(wyn)







