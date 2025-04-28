f = open("liczby.txt")
count = [["0",0],["1",0],["2",0],["3",0],["4",0],["5",0],["6",0],["7",0],["8",0],["9",0],["A",0],["B",0],["C",0],["D",0],["E",0],["F",0]]
total = 0
for line in f:
    line = line.replace("	","").replace("\n","")
    for character in line:
        for i in range(0,len(count)):
            if character==count[i][0]:
                count[i][1]+=1
                total+=1
                break
for key,val in count:
    print(key + ": "+str(round((val/total)*100,2))+"%")