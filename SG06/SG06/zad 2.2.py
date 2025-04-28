f = open("liczby.txt")
results = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
for line in f:
    left = line.split("	")[0]
    right = line.split("	")[1]
    for system in range(2,17):
        try:
            numberOne = str(int(left,system))
            numberTwo = str(int(right,system))[::-1]
            if(numberOne==numberTwo):
                results[system]+=1
        except:
            continue
for system in range(2,17):
    print(str(system)+": "+str(results[system]))