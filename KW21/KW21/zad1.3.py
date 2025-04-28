def negacja(c):
    w = ""
    for i in c:
        if i == "0":
            w += "1"
        else:
            w += "0"
    return w

def transformacja(S, k):
    if k == 0:
        return S
    T = transformacja(S, k - 1)
    N = negacja(T)
    return T+N


print(transformacja("0", 4))

ciag = transformacja("0", 4)
print(len(ciag))
wycinki_unikalne = []

for i in range(len(ciag)-3):
    wycinek = ciag[i:i+4]
    if wycinek not in wycinki_unikalne:
        wycinki_unikalne.append(wycinek)

print(wycinki_unikalne)
print(len(wycinki_unikalne))
