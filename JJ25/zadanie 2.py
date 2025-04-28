filepath=r"C:\Users\jaasi\OneDrive\Pulpit\AGH\pliki\pliki (1)\liczby.txt"
plik=open(filepath,"r")
liczby1=[]
liczby2=[]
for i in plik:
    a,b=i.split()
    liczby1.append(a)
    liczby2.append(b.strip())
systemy=[]
#2
for i in range(0,len(liczby1)):
    for x in range(2,17):
        try:
            if str(int(liczby1[i],x)) == str(int(liczby2[i],x))[::-1]:
                systemy.append(x)
        except:
            pass
print("zad 2")
for i in range(2,17):
    print(i,":",systemy.count(i))

#3
print("zad 3")
maxi=0
mini=10000000000
znakm=0
maxznak=0
for i in range(0,len(liczby1)):
    if int(liczby1[i],systemy[i])<mini:
        mini=int(liczby1[i],systemy[i])
        znakm=liczby1[i]
    if int(liczby1[i],systemy[i])>maxi:
        maxi=int(liczby1[i],systemy[i])
        maxznak=liczby1[i]
    if int(liczby2[i],systemy[i])<mini:
        mini=int(liczby2[i],systemy[i])
        znakm=liczby2[i]
    if int(liczby2[i],systemy[i])>maxi:
        maxi=int(liczby2[i],systemy[i])
        maxznak=liczby2[i]
print(znakm,maxznak)

#4
print("zad 4")
znaki=[]
for i in liczby1:
    for x in i:
        znaki.append(x)
for i in liczby2:
    for x in i:
        znaki.append(x)
suma=len(znaki)
for i in range(48,58):
    print(chr(i),":",round(znaki.count(chr(i))/suma*100,2),"%")
for i in range(65,71):
    print(chr(i), ":", round(znaki.count(chr(i)) / suma * 100, 2),"%")





