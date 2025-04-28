f = open("liczby.txt")
mini = 9999999999999999
maxi = 0
resultmini = ""
resultmaxi = ""
for line in f:
    left = line.split("	")[0]
    right = line.split("	")[1].replace("\n","")
    for system in range(2,17):
        try:
            numberOne = int(left,system)
            numberTwo = int(right,system)
            if(str(numberOne)==str(numberTwo)[::-1]):
                if(numberOne<mini):
                    mini = numberOne
                    resultmini = left
                if(numberOne>maxi):
                    maxi = numberOne
                    resultmaxi = left
                if(numberTwo<mini):
                    mini = numberTwo
                    resultmini = right
                if(numberTwo>maxi):
                    maxi = numberTwo
                    resultmaxi = right
        except:
            continue
print(resultmini + " " + resultmaxi)