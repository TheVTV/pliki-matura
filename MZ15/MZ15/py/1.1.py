def negacja(c):
    w = ""
    for z in c:
        if z == "0":
            w += "1"
        else:
            w += "0"
    return w

def transformacja(s,k):
    if k == 0:
        return s
    else:
        t = transformacja(s,k-1)
        n = negacja(t)
        return t + n

print(transformacja("0",7))