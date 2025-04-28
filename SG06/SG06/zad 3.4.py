f = open("kebab.txt")
falafel = 0
for line in f:
    line = line.replace("\n","")
    number = int(line)
    lastNumber = 0
    kebab = number
    while(True):
        czynnik = 2
        czynniki = []
        while czynnik*czynnik <= number:
            while number % czynnik == 0:
                czynniki.append(czynnik)
                number = number/czynnik
            czynnik+=1
        if(number>1):
            czynniki.append(int(number))
        newNumber = 0
        for czyn in czynniki:
            newNumber+=czyn
        kebab+=newNumber
        if(newNumber==lastNumber):
            break
        else:
            number = newNumber
            lastNumber = number
    dzielniki = []
    for dzielnik in range(1,kebab):
        if kebab % dzielnik == 0:
            dzielniki.append(dzielnik)
    suma = 0
    for dzielnik in dzielniki:
        suma+=dzielnik
    if(suma==kebab):
        falafel+=1
    

print(falafel)