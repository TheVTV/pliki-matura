f = open("kebab.txt")
count = 0
for line in f:
    line = line.replace("\n","")
    number = int(line)
    parzyste = 0
    nieparzyste = 0
    lastNumber = 0
    if(number%2==0):
        parzyste+=1
    else:
        nieparzyste+=1
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
        if(newNumber%2==0):
            parzyste+=1
        else:
            nieparzyste+=1
        if(newNumber==lastNumber):
            break
        else:
            number = newNumber
            lastNumber = number
    if(parzyste==nieparzyste):
        count+=1
    
print(count)