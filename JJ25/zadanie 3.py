import math
filepath=r"C:\Users\jaasi\OneDrive\Pulpit\AGH\pliki\pliki (1)\kebab.txt"
plik=open(filepath,"r")
liczby=[]
for i in plik:
    liczby.append(int(i.strip()))

def sumarozklad(n):
    czynniki=[]
    while n>1:
        for i in range(2,n+1):
            if n%i==0:
                czynniki.append(i)
                n//=i
                break
    suma=0
    for i in czynniki:
        suma+=i
    return suma

def kebab(n):
    licznik=1
    while(n!=sumarozklad(n)):
        licznik+=1
        n=sumarozklad(n)
    return licznik+1

def palindrom(n):
    if str(n)==str(n)[::-1]:
        return True
    return False
def isprime(n):
    if n<2:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

#1
maxi=0
maxkebab=[]
for i in liczby:
    if kebab(i)>maxi:
        maxkebab.clear()
        maxi=kebab(i)
        maxkebab.append(i)
    if kebab(i)==maxi:
        maxkebab.append(i)
print("zad 1")
print(maxi)
for i in set(maxkebab):
    print(i)

def liczbakebabowa(n):
    licznik=n
    while(n!=sumarozklad(n)):
        licznik+=sumarozklad(n)
        n=sumarozklad(n)
    return licznik+n
#2
liczbykebabowe=[]
for i in liczby:
    liczbykebabowe.append(liczbakebabowa(i))
pierwsze=0
palindromy=0
for i in liczbykebabowe:
    if isprime(i):
        pierwsze+=1
    if palindrom(i):
        palindromy+=1
print("zad 2")
print(palindromy,pierwsze)

#3
def np(n):
    p=0
    nie=0
    if n%2==0:
        p+=1
    else:
        nie+=1
    while(n!=sumarozklad(n)):
        n=sumarozklad(n)
        if n%2==0:
            p+=1
        else:
            nie+=1
    if n%2==0:
        p+=1
    else:
        nie+=1
    if p==nie:
        return True
    else:
        return False
print("zad 3")
licznik=0
for i in liczby:
    if np(i)==True:
        licznik+=1
print(licznik)

#4
def dzielnikiwlasciwe(n):
    suma=0
    if n==1:
        return 1
    for i in range(1,n):
        if n%i==0:
            suma+=i
    return suma
licznik=0
for i in liczbykebabowe:
    if dzielnikiwlasciwe(i)==i:
        licznik+=1
print("zad 4")
print(licznik)