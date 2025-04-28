file = open("dane/kebab.txt")
lines = file.readlines()
file.close()

def isPrime(n):
    n = int(n)
    if n < 2:
        return False
    else:
        for i in range(2,int(n**0.5) + 1):
            if n % i == 0:
                return False
    return True

def genPrimes(a):
    p = []
    for i in range(a+1):
        if isPrime(i):
            p.append(i)
    return p

def primeDiv(a):
    primes = genPrimes(a)
    t = []
    i = 0
    atmp = a
    while atmp > 1:
        if atmp % primes[i] == 0:
            atmp = atmp // primes[i]
            t.append(primes[i])
        else: i += 1
    return t

def czyPalindrom(a):
    atmp = str(a)
    i = int(len(atmp) / 2)

    if len(atmp) % 2 == 0:
        for j in range(i):
            if atmp[j] != atmp[len(atmp) - j - 1]:
                return False
    else:
        for j in range(i):
            if atmp[j] != atmp[len(atmp) - j - 1]:
                return False
    return True

currentKebab = 0
prevNum = 0

currentSumaKebab = 0

palindromy = 0
primes = 0

for line in lines:
    a = int(line)

    atmp = a
    currentKebab = 0
    currentSumaKebab = 0

    while True:
        # rozbij na czynniki pierwsze
        t = primeDiv(atmp)

        # sumuj
        currentSumaKebab += atmp
        atmp = sum(t)

        currentKebab += 1

        if prevNum == t:
            break

        prevNum = t

    if czyPalindrom(currentSumaKebab):
        palindromy += 1
    if isPrime(currentSumaKebab):
        primes += 1

print(palindromy, primes)
