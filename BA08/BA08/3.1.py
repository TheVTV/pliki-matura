def Czynniki(n):
    suma = 0

    while n != 1:
        i = 2
        while n % i != 0:
            i+=1
        n = n//i
        suma += i
    return suma



def zwijanie(kroki, n):
    if Czynniki(Czynniki(n)) == Czynniki(n):
        return kroki+3
    else:
        kroki += 1
        n = Czynniki(n)
        return zwijanie(kroki, n)

print(zwijanie(0, 60))

f=open("kebab_przyklad.txt")
liczby = [0]*15

najk = 0
for line in f:
    if zwijanie(0, line)>najk:
        najk = zwijanie(kroki, line)
print(najk)