f = open("kebab.txt")
palindromy = 0
pierwsze = 0
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
    stringKebab = str(kebab)
    busted = False
    for i in range(0,len(stringKebab)):
        if(stringKebab[i]!=stringKebab[len(stringKebab)-(i+1)]):
            busted = True
            break
    if not busted:
        palindromy+=1
    temp = kebab
    busted = False
    czynnik = 2
    while czynnik != temp:
        while temp % czynnik == 0:
            busted = True
            break
        czynnik+=1
    if(not busted):
        pierwsze+=1

print(str(palindromy) + ' ' + str(pierwsze))