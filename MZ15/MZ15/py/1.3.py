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
t = transformacja("0",7)
print(t)

# zlicz najdluzszy fragment
maxFrag = 0
currentFrag = 0
prevFrag = ""
for z in range(len(t)):
    if z == 0:
        currentFrag += 1
        prevFrag = t[z]
    else:
        if prevFrag == t[z]:
            currentFrag += 1
        else:
            prevFrag = t[z]

            if currentFrag > maxFrag:
                maxFrag = currentFrag
            currentFrag = 1

print(maxFrag)