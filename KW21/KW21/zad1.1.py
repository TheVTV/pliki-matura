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

print(transformacja("0", 3))
print(transformacja("1", 2))
print(transformacja("01", 3))
print(transformacja("101", 3))