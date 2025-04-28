plik = open(".\kebab_przyklad.txt", "r")
linie = plik.readlines()
linie_gotowe = []
for i in linie:
    linie_gotowe.append(int(i[:-1]))
print(linie_gotowe)

# def isPrime(n):
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

def zwiniecie(n, D, S):
    d = 0
    t = []
    while n > 1:
        for i in range(2, n+1):
            if n % i == 0:
                t.append(i)
                n = n // i
                d += 1
                break
    print(sum(t), D, S + sum(t))
    if d == 1:
        return sum(t), D, S+sum(t)
    return zwiniecie(sum(t), D+1, S+sum(t))

def proces_zwijania(n):
    if zwiniecie(n)[1] == 1:
        pass



print(zwiniecie(60, 0, 60))

d_max, num_max = 0, []
for i in linie_gotowe:
    wynik = zwiniecie(i, 0, i)
    if wynik[1] > d_max:
        d_max, num_max = wynik[1], [i]
    elif wynik == d_max:
        num_max.append(i)
print(d_max, num_max)


with open("wyniki3.txt", "w") as f:
    f.write("3.1\n")

plik.close()