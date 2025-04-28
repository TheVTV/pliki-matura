z = ["1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
zab = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

def liczbaSystemow(n):
    maxSystem = 16

    for i in n:
        for j in range(15):
            if i == z[j]:
                if maxSystem > 15 - j:
                    maxSystem = 15 - j

    return(maxSystem)

def liczNa10(n,s):
    pot = 0
    w = 0
    ntmp = n

    while ntmp != "":
        # liczba jednosci
        x = ntmp[-1:len(ntmp)]

        # utnij
        ntmp = ntmp[0:-1]

        # znajdz wartość liczby jednosci
        i = zab.index(x)

        w += pow(s,pot)*i
        pot += 1

    return w

def obroc(w):
    t = ""
    for x in str(w):
        t = x + t

    return int(t)

def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

l = {}

for i in range(2,17):
    l[i] = 0

# print(l)

file = open("dane/liczby.txt")
lines = file.readlines()
file.close()

for line in lines:
    a = str(line.split("\t")[0])
    b = str(line.split("\t")[1].split("\n")[0])

    sysA = 17 - liczbaSystemow(a)
    sysB = 17 - liczbaSystemow(b)

    maxSys = 0

    if sysA >= sysB:
        maxSys = sysA
    elif sysA < sysB:
        maxSys = sysB

    # sprawdz warunek
    while True:

        # przelicz na 10
        bw = liczNa10(b,maxSys)
        aw = liczNa10(a,maxSys)

        # sprawdz czy druga odwrocona jest taka jak piwrwsza
        bw = obroc(bw)

        if bw == aw:
            # to ten system
            l[maxSys] += 1
            break
        else:
            # nie ten szukamy wyżej
            maxSys += 1

for i in l:
    print(i,":",l[i])
