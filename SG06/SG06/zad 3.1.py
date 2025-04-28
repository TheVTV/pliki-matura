f = open("kebab.txt")
maxi = 0
maxiLiczby = []
for line in f:
    line = line.replace("\n","")
    number = int(line)
    count = 1
    lastNumber = 0
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
        count+=1
        newNumber = 0
        for czyn in czynniki:
            newNumber+=czyn
        if(newNumber==lastNumber):
            break
        else:
            number = newNumber
            lastNumber = number
    if(count>maxi):
        maxi = count
        maxiLiczby = [line]
    elif(count==maxi):
        maxiLiczby.append(line)
print(maxi)
for liczba in maxiLiczby:
    print(liczba)