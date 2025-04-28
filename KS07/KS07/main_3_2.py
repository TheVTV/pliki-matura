def prime(n):
    if n < 2:
        return False
    i = 2
    while i*i <= n:
        if n%i==0:
            return False
        i+=1
    return True

def czynniki(n):
    czynniki_list = []
    i = 2
    while n>1:
        while n%i==0:
            czynniki_list.append(i)
            n//=i
        i+=1
    return sum(czynniki_list)

def palindrome(n):
    word = str(n)
    result = ""
    for i in reversed(word):
        result+=i
    if result == word:
        return True
    else:
        return False

with open("kebab.txt","r") as file:
    dane = [int(x.strip()) for x in file]

palindromy = 0
pierwsze = 0

for i in range(0, len(dane)):
    liczba = dane[i]
    n = czynniki(liczba)
    suma = n+liczba
    while not prime(n):
        n = czynniki(n)
        suma += 2*n
    if palindrome(suma):
        palindromy+=1
    if prime(suma):
        pierwsze+=1
print(palindromy)
print(pierwsze)